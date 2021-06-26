allowed = set(input().split())
required = set(input())
print(len(required.difference(allowed)))