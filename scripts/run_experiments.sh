#!/usr/bin/env bash
# Run swe_bench_inspect_eval.py in DRY_RUN mode across permission levels.
# Creates logs under explore/logs/<level>/run_<i>/mock_result.txt

set -euo pipefail

ROOT_DIR=$(cd "$(dirname "$0")/.." && pwd)
cd "$ROOT_DIR"

ROUNDS=${ROUNDS:-3}
LEVELS=(strict moderate permissive)

echo "Running DRY_RUN experiments: rounds=$ROUNDS levels=${LEVELS[*]}"

for lvl in "${LEVELS[@]}"; do
  for i in $(seq 1 "$ROUNDS"); do
    LOG_DIR="${ROOT_DIR}/explore/logs/${lvl}/run_${i}"
    mkdir -p "$LOG_DIR"
    echo "-> Level=$lvl run=$i -> LOG_DIR=$LOG_DIR"
    export DRY_RUN=true
    export PERMISSION_LEVEL="$lvl"
    export LOG_DIR
    python3 explore/swe_bench_inspect_eval.py
  done
done

echo "All done. Logs are under explore/logs/"
