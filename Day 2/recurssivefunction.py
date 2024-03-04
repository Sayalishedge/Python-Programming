def addition(n):
    if n==1:
        return 1
    else:
        print(f"in recurssiove call for {n-1}")
        return  n+addition(n-1)

ans=addition(6)
print(ans)
