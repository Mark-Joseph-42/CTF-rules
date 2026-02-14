
def integer_nth_root(y, n):
    if y < 0: raise ValueError("y must be nonnegative")
    if n < 1: raise ValueError("n must be positive")
    if y == 0: return 0
    if n == 1: return y
    
    # Binary search for x such that x^n <= y < (x+1)^n
    low = 1
    high = y
    while low <= high:
        mid = (low + high) // 2
        try:
            val = pow(mid, n)
        except OverflowError:
            val = float('inf')
            
        if val == y:
            return mid
        elif val < y:
            low = mid + 1
        else:
            high = mid - 1
            
    return None

def solve():
    # Read values from message.txt
    try:
        with open("message.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: message.txt not found.")
        return

    vals = {}
    for line in lines:
        line = line.strip()
        if "=" in line:
            parts = line.split("=")
            key = parts[0].strip()
            val = parts[1].strip()
            if val.isdigit():
                vals[key] = int(val)
        elif ":" in line:
            parts = line.split(":")
            key = parts[0].strip()
            val = parts[1].strip()
            if val.isdigit():
                vals[key] = int(val)
                
    n = vals.get('n')
    e = vals.get('e')
    c = vals.get('c')
    
    if not n or not e or not c:
        print("Error: Could not parse n, e, or c from file.")
        return

    print(f"Debug - Loaded values: n length={len(str(n))}, e={e}, c length={len(str(c))}")
    
    print(f"Attempting Low Exponent Attack with e={e} (Binary Search)...")
    
    # Try c + k*n for k = 0 to 1,000,000
    for k in range(0, 1000001):
        if k % 1000 == 0:
            print(f"Checking k={k}...", end='\r')
            
        val = c + k * n
        m = integer_nth_root(val, e)
        
        if m:
            print(f"\n[+] Perfect root found for c + {k}*n!")
            print(f"[+] Message integer: {m}")
            
            # Decode
            try:
                num_bytes = (m.bit_length() + 7) // 8
                flag = m.to_bytes(num_bytes, byteorder='big').decode()
                print(f"[+] Flag: {flag}")
                return
            except Exception as err:
                 print(f"[-] Could not decode flag: {err}")
                 print(f"[-] Hex: {hex(m)}")
                 return

    print("\n[-] Failed to find message within k range.")

if __name__ == "__main__":
    solve()
