def tower(n,src,help,dest):
    if n==1:
        print(f"move disk from {src} to {dest}")
        return
    tower(n-1,src,dest,help)#moving n-1 disks from src to helper
    print(f"Move disk {n} from {src} to {dest}")
    tower(n-1,help,src,dest)
tower(3,"A","B","C")