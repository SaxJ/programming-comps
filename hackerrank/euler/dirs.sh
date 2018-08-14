n=5;
max=50;
while [ "$n" -le "$max" ]; do
  mkdir "euler$n"
  n=`expr "$n" + 1`;
done
