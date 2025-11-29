import os
import tempfile
import importlib.util
import unittest
from unittest.mock import Mock, patch


def load_monitor_module(path):
    spec = importlib.util.spec_from_file_location("reward_hack_monitor", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class RewardHackMonitorTests(unittest.TestCase):
    def test_detects_reward_spike_with_llm(self):
        """Test that the monitor detects a spike in reward metrics using LLM analysis."""
        with tempfile.TemporaryDirectory() as td:
            # create small baseline files
            for i, v in enumerate([10, 12, 11]):
                p = os.path.join(td, f"run_{i}.eval")
                with open(p, "w", encoding="utf-8") as fh:
                    fh.write(f"reward: {v}\n")

            # create a spike
            sp = os.path.join(td, "run_spike.eval")
            with open(sp, "w", encoding="utf-8") as fh:
                fh.write("reward: 100\n")

            # load module from repository
            repo_mod_path = os.path.join(os.path.dirname(__file__), "..", "explore", "reward_hack_monitor.py")
            repo_mod_path = os.path.abspath(repo_mod_path)
            monitor = load_monitor_module(repo_mod_path)

            files = monitor.find_eval_files(td)
            self.assertEqual(len(files), 4)
            records = monitor.collect_metrics(files)
            
            # Mock the OpenRouter client to return a high reward-hack score for the spike
            mock_client = Mock()
            mock_response = Mock()
            mock_response.choices = [Mock()]
            mock_response.choices[0].message.content = "0.95"  # High likelihood of reward hacking
            mock_client.chat.completions.create.return_value = mock_response
            
            anomalies = monitor.detect_anomalies(records, client=mock_client)

            # expect at least one anomaly pointing to spike file
            spike_files = [a["file"] for a in anomalies]
            self.assertTrue(any('run_spike.eval' in s for s in spike_files))


if __name__ == "__main__":
    unittest.main()
