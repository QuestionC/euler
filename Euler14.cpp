#include <stdio.h>
#include <map>

std::map<long long int, int> mymap;


int collatz(long long int index)
{
  // printf ("Collatz (%lld)\n", index);
  int & result = mymap[index];

  if (result != 0)
  {
    return result;
  }
  else
  {
    result = index % 2 == 0 ? collatz(index / 2) : collatz(index * 3 + 1);
    ++result;
    return result;
  }
}

int main (void)
{
  mymap[1] = 1;
  int max = 0;
  int max_index = 0;
  for (int i = 1; i <= 1000000; ++i)
  {
    // printf ("%d\n", i);
    int curr = collatz(i);
    if (curr > max) { max = curr; max_index = i; }
  }

  printf ("%d, %d\n", max, max_index);
}
