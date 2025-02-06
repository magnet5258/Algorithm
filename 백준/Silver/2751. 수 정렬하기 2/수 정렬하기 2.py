import sys
N = int(sys.stdin.readline())
lst = sorted(map(int, sys.stdin.read().split()))
sys.stdout.write("\n".join(map(str, lst)) + "\n")
