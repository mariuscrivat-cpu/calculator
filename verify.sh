#!/usr/bin/env bash
# Verificare locala (CI local). Contract folosit de orchestrator:
#   - exit 0 = testele trec
#   - cate o linie `TEST: <nume test>` pentru fiecare test rulat
#   - ultima linie: TESTS_COUNT=<numar de teste rulate>
set -uo pipefail

out=$(python3 -m unittest discover -v 2>&1)
status=$?
echo "$out"

echo "$out" | grep -E ' \.\.\. ' | sed -E 's/ \.\.\. .*//; s/^/TEST: /'
count=$(echo "$out" | grep -Eo '^Ran [0-9]+ test' | grep -Eo '[0-9]+' | head -1)
echo "TESTS_COUNT=${count:-0}"
exit "$status"
