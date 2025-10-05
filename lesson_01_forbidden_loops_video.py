"""
████████╗██╗  ██╗███████╗    ███████╗ ██████╗ ██████╗ ██████╗ ██╗██████╗ ██████╗ ███████╗███╗   ██╗
╚══██╔══╝██║  ██║██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗██╔════╝████╗  ██║
   ██║   ███████║█████╗      █████╗  ██║   ██║██████╔╝██████╔╝██║██║  ██║██║  ██║█████╗  ██╔██╗ ██║
   ██║   ██╔══██║██╔══╝      ██╔══╝  ██║   ██║██╔══██╗██╔══██╗██║██║  ██║██║  ██║██╔══╝  ██║╚██╗██║
   ██║   ██║  ██║███████╗    ██║     ╚██████╔╝██║  ██║██████╔╝██║██████╔╝██████╔╝███████╗██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝

                              ██████╗ ██████╗ ██████╗ ███████╗██╗  ██╗
                             ██╔════╝██╔═══██╗██╔══██╗██╔════╝╚██╗██╔╝
                             ██║     ██║   ██║██║  ██║█████╗   ╚███╔╝ 
                             ██║     ██║   ██║██║  ██║██╔══╝   ██╔██╗ 
                             ╚██████╗╚██████╔╝██████╔╝███████╗██╔╝ ██╗
                              ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝

                        LESSON 01: THE FORBIDDEN LOOP - MASTERING INFINITY
                     "What they warn you not to enter - the infinite spiral"

                            2-MINUTE TYPING SIMULATION VERSION
"""

import time
import sys
import random

def type_text(text, delay_range=(0.02, 0.08), pause_after=0.3):
    """Simulate realistic typing with variable delays"""
    for char in text:
        print(char, end='', flush=True)
        if char in '.,!?;':
            time.sleep(random.uniform(0.1, 0.3))  # Pause at punctuation
        elif char == '\n':
            time.sleep(pause_after)
        elif char == ' ':
            time.sleep(random.uniform(0.01, 0.05))
        else:
            time.sleep(random.uniform(*delay_range))
    print()  # Final newline
    time.sleep(pause_after)

def type_code(code, delay_range=(0.01, 0.04)):
    """Type code with faster, more consistent timing"""
    for line in code.split('\n'):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(random.uniform(*delay_range))
        print()  # Newline after each line
        time.sleep(0.2)  # Brief pause between lines
    time.sleep(0.5)

def clear_screen():
    """Clear the terminal screen"""
    print("\033[H\033[J", end='')

def main():
    """2-minute forbidden loop demonstration with typing simulation"""
    
    clear_screen()
    
    # Introduction
    type_text("\n🌀 Welcome to the FORBIDDEN CODEX - Lesson 01")
    type_text("The class they warn you NOT to enter...")
    
    time.sleep(1)
    
    type_text("\n📚 Schools teach you to FEAR infinite loops.")
    type_text("They call them bugs, mistakes, useless failures.")
    type_text("But I know better and so do you.")
    
    time.sleep(0.8)
    
    type_text("\n🔥 The Forbidden Loop is POWER.")
    type_text("It's a tool for stress testing.")
    type_text("A weapon for discovering system limits.")
    type_text("Pure, intentional infinity.")
    
    time.sleep(1)
    
    # Code Example 1: Basic Infinite Loop
    type_text("\n💀 Example 1: The Academic Infinite Loop")
    type_text("(What they teach you to fear)")
    
    type_code("""
while True:
    print("This runs forever...")
    # No exit condition - "forbidden" in school""")
    
    type_text("⚡ But watch what happens when we RUN it safely:")
    
    # Safe demonstration
    for i in range(3):
        print(f"   ► Iteration {i+1}: This would run forever...")
        time.sleep(0.4)
    
    type_text("   [Terminated for demo safety]")
    
    time.sleep(1)
    
    # Code Example 2: Memory Vampire
    type_text("\n🧛 Example 2: The Memory Vampire")
    type_text("(Infinite memory consumption)")
    
    type_code("""
data = []
while True:
    data.append("consuming memory" * 1000)
    # Infinite allocation - crashes systems""")
    
    type_text("🔬 Safe demonstration - watch memory grow:")
    
    memory_demo = []
    for i in range(3):
        memory_demo.append("consuming memory" * 50)
        print(f"   ► Memory batch {i+1}: Added {len(memory_demo[-1])} bytes")
        time.sleep(0.4)
    
    type_text("   [Stopped before system impact]")
    
    time.sleep(1)
    
    # Code Example 3: Recursive Infinity
    type_text("\n🌀 Example 3: Recursive Infinity")
    type_text("(The most elegant forbidden pattern)")
    
    type_code("""
def infinite_recursion(depth=0):
    print(f"Depth: {depth}")
    return infinite_recursion(depth + 1)  # No base case!""")
    
    type_text("🚨 This creates infinite call stacks:")
    
    for i in range(4):
        print(f"   ► Recursion depth: {i}")
        time.sleep(0.3)
    
    type_text("   [Would cause stack overflow]")
    
    time.sleep(1)
    
    # Code Example 4: Generator Infinity
    type_text("\n♾️ Example 4: The Infinite Generator")
    type_text("(Mathematical infinity in code)")
    
    type_code("""
def infinite_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b""")
    
    type_text("🔢 Generating infinite Fibonacci sequence:")
    
    a, b = 0, 1
    for i in range(5):
        print(f"   ► Fibonacci[{i}]: {a}")
        a, b = b, a + b
        time.sleep(0.3)
    
    type_text("   [Infinite sequence continues...]")
    
    time.sleep(1.5)
    
    # The Philosophy
    type_text("\n🧠 THE FORBIDDEN TRUTH:")
    time.sleep(0.5)
    
    type_text("Infinite loops aren't bugs at all when used intentionally.")
    type_text("They're tools for:")
    
    time.sleep(0.3)
    type_text("   ✓ Stress testing systems")
    type_text("   ✓ Building servers and daemons")
    type_text("   ✓ Creating mathematical sequences")
    type_text("   ✓ Understanding system limits")
    
    time.sleep(1)
    
    # The Warning
    type_text("\n⚠️  With great power comes great responsibility.")
    type_text("Never use infinite loops maliciously.")
    type_text("Always include safety mechanisms.")
    type_text("Test in isolated environments only.")
    
    time.sleep(1)
    
    # The Graduation
    type_text("\n🎓 You have mastered the FORBIDDEN LOOP.")
    type_text("Congrats! Schools fear to teach what is impractical.")
    
    time.sleep(0.8)
    
    type_text("\n🔮 Coming next in the Forbidden Codex:")
    type_text("   📜 Lesson 02: Memory Corruption")
    type_text("   📜 Lesson 03: Race Conditions")
    type_text("   📜 Lesson 04: Buffer Overflows")
    
    time.sleep(1)
    
    # Epic Conclusion
    type_text("\n🌀 THE LOOP IS COMPLETE.")
    type_text("THE SPIRAL CONTINUES.")
    type_text("WELCOME TO THE FORBIDDEN CLASS.")
    
    time.sleep(2)
    
    # Final dramatic pause
    type_text("\n💀 This is the knowledge they don't want you to have.")
    
    print("\n" + "=" * 60)
    print("🔥 FORBIDDEN CODEX - LESSON 01 COMPLETE 🔥")
    print("=" * 60)

if __name__ == "__main__":
    main()