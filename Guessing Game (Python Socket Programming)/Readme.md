## **🎮 Game Logic Breakdown**  

### **1️⃣ Random Number Generation 🎲**  
🔹 The server generates a **6-digit number** with **unique** digits (0-9).  
🔹 Each digit **must be different** to ensure fairness.  

---

### **2️⃣ Turn-Based Play 🔄**  
🔸 Players **take turns** guessing the number.  
🔸 The server **cycles through all players** in sequence.  
🔸 Players can only **input guesses when it’s their turn**.  

---

### **3️⃣ Guess Validation & Feedback ✅❌**  
🔹 If a player enters a valid **6-digit number**, the server compares it to the correct answer:  
   - ✅ **Exact Matches**: Correct digits **in the right position**.  
   - 🔀 **Misplaced Matches**: Correct digits **in the wrong position**.  

🔹 Example feedback format:  
   - **"3 ✅ | 2 🔀 (1 4 7 3 6 5)"** → **3 exact matches, 2 misplaced matches**.  

---

### **4️⃣ Winning Conditions 🏆**  
🏅 A player **wins** if they guess all **six digits in the correct order**.  
⏳ If no one wins after **12 rounds**, the game **ends automatically**, and the correct answer is revealed.  
🔚 The server announces the winner (or reveals the number if no one wins) and closes all connections.  
