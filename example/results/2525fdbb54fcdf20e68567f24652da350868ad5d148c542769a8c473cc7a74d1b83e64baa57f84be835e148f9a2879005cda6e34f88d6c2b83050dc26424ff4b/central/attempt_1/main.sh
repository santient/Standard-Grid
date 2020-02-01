cd ./groups/
cat group_0.sh | xargs -L 1 -I CMD -P 1 bash -c CMD &
cd - > /dev/null
cd ./groups/
cat group_1.sh | xargs -L 1 -I CMD -P 1 bash -c CMD &
cd - > /dev/null
cd ./groups/
cat group_2.sh | xargs -L 1 -I CMD -P 1 bash -c CMD &
cd - > /dev/null
cd ./groups/
cat group_3.sh | xargs -L 1 -I CMD -P 1 bash -c CMD &
cd - > /dev/null
cd ./groups/
cat group_4.sh | xargs -L 1 -I CMD -P 1 bash -c CMD &
cd - > /dev/null
cd ./groups/
cat group_5.sh | xargs -L 1 -I CMD -P 1 bash -c CMD &
cd - > /dev/null
cd ./groups/
cat group_6.sh | xargs -L 1 -I CMD -P 1 bash -c CMD &
cd - > /dev/null
cd ./groups/
cat group_7.sh | xargs -L 1 -I CMD -P 1 bash -c CMD &
cd - > /dev/null
wait