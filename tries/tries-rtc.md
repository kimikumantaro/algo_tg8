# TRIES Running Time Complexity

n = maximum string length

## Main Class

| Cost | Time |
|:-:|:-:|
| c1 | 1 |
| c2 | 1 |
| c3 | 1 |
| c4 | 1 |
| c5 | 1 |
| c6 | 1 |
| c7 | 1 |
| c8 | 1 |
| c9 | 1 |

Running Time, T(N) = c1(1) + c2(1) + c3(1) + c4(1) + c5(1) + c6(1) + c7(1) + c8(1) + c9(1)

Therefore, the time complexity of this class can be said to be O(1).

## TrieNode Class

| Cost | Time |
|:-:|:-:|
| c1 | 1 |

Running Time, T(N) = c1(1)

Therefore, the time complexity of this class can be said to be O(1).

## Trie Class

### Insert Function

| Cost | Time |
|:-:|:-:|
| c1 | n |
| c2 | n-1 |
| c3 | n*n |
| c4 | n(n-1) |
| c5 | 1 |
| c6 | n(n-1) |
| c7 | n(n-1) |
| c8 | n-1 |

Running Time, T(N) = c1(n) + c2(n-1) + c3(n*n) + c4(n(n-1)) + c6((n(n-1)) + c7(n(n-1)) + c8(n-1)

Therefore, the time complexity of this class can be said to be O(n^2).

### Search Function

| Cost | Time |
|:-:|:-:|
| c1 | 1 |
| c2 | n |
| c3 | n-1 |
| c4 | 1 |
| c5 | n-1 |
| c6 | 1 |
| c7 | 1 |

Running Time, T(N) = c2(n) + c3(n-1) + c5(n-1)

Therefore, the time complexity of this class can be said to be O(n).
