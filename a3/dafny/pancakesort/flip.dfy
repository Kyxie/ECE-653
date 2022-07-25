// flips (i.e., reverses) array elements in the range [0..num]
method flip (a: array<int>, num: int)
  requires a != null && a.Length > 0;
  requires 0 <= num < a.Length;
  modifies a;
  ensures multiset(old(a[..])) == multiset(a[..]);
  ensures forall p :: 0 <= p <= num  ==> a[p] == old(a[num-p]);
  ensures forall p :: num < p < a.Length ==> a[p] == old(a[p]);
{
  var tmp:int;
  var i := 0;
  var j := num;
  while (i < j)
    decreases num - i;
    invariant i + j ==num;
    invariant 0 <= i <= num/2 + 1;
    invariant num/2-1 <= j <=num;
    invariant multiset(old(a[..])) == multiset(a[..]);
    invariant forall p :: 0<= p <i ==> a[p] == old(a[num-p]);
    invariant forall p :: num < p < a.Length ==> a[p] == old(a[p]);
    invariant forall p :: 0<= p <i ==> a[num-p] == old(a[p]);
    invariant forall p :: i<= p <= j ==> a[p] == old(a[p]);
  {
    tmp := a[i];
    a[i] := a[j];
    a[j] := tmp;
    i := i + 1;
    j := j - 1;
  }
}
