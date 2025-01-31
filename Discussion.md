# **Discussion.md**

## **Solutions Considered**

### **1️ Reading the Entire File into Memory**
- Approach: Load the entire `logs_2024.log` file into memory and use string operations to filter logs by date.
- Pros: Simple and easy to implement.
- Cons: Not feasible for large files (1TB+), leading to **high memory usage** and potential system crashes.

### **2️ Line-by-Line Streaming (Final Approach)**
- Approach: Open the file and read it **line by line**, checking if the line starts with the target date.
- Pros: Memory-efficient, Works for large files (1TB+), Faster as it avoids unnecessary data loading.
- Cons: Slightly slower than in-memory filtering but negligible in real-world use.

### **3️ Using Grep (Command Line Optimization)**
- Approach: Use system commands like `grep` (Linux/Mac) or `findstr` (Windows) to filter logs.
- Pros: Fastest method as it utilizes OS-level optimizations.
- Cons: Not cross-platform, requires additional dependencies.

---

We chose the line-by-line streaming approach because:
- It optimizes for speed and memory usage.
- It works on all operating systems (Windows, Mac, Linux).
- It does not require external dependencies.
- It correctly saves extracted logs in the `output/` folder.

---

## **Steps to Run**

### **1️⃣ Prerequisites**
- Ensure **Python 3** is installed.
- Place `logs_2024.log` inside `tech-campus-recruitment-2025/`.

### **2️⃣ Running the Script**
1. Open **Terminal/Command Prompt**.
2. Navigate to the project folder:
   ```sh
   cd tech-campus-recruitment-2025/src
   ```
3. Run the script:
   ```sh
   python hi.py
   ```
4. Enter the target date (YYYY-MM-DD) when prompted:
   ```
   Enter the date (YYYY-MM-DD) to extract logs: 2024-02-22
   ```
5. The logs will be saved in:
   ```
   tech-campus-recruitment-2025/output/output_2024-02-22.txt
   ```

---

## **Link to Forked Repository**
[👉 Your GitHub Repository Link Here 👈]

---

This **ensures an efficient and scalable solution** for large log file extraction. 🚀

