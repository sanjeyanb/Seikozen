# Smart Supply Chain Monitoring System (Pharmaceutical Focus)

## 📌 Overview
This project proposes a **Smart Supply Chain Monitoring System** that enhances transparency, security, and accountability across the pharmaceutical supply chain.  
Our solution combines **hardware + software** with a **hybrid blockchain model** (public + private) to tackle three major challenges in pharma logistics:
1. ✅ Quality Assurance  
2. ⚠️ Risk Management  
3. 🛡️ Counterfeit Prevention  

---

## 🚩 Problem Statement
The Indian pharmaceutical market is worth **₹1.8 trillion**, yet nearly **37% of products are wasted**, with **₹10,000 crore lost during transport alone**.  
Key issues include:
- Lack of **real-time monitoring** during transportation.  
- **Unclear accountability** in case of damage or spoilage.  
- Rising cases of **counterfeit medicines** entering the supply chain.  

---

## 💡 Proposed Solution
We introduce a **hybrid hardware–software monitoring system** that:
- Collects **real-time consignment data** during transport & storage.  
- Stores and validates data on a **hybrid blockchain**:  
  - **Public Blockchain** → Transparency & verification  
  - **Private Blockchain** → Secure access for authorized parties  
- Ensures **quality assurance, risk reduction, and counterfeit prevention**.  

---

## 🛠️ Tech Stack

### 🔹 Hardware Components
- **Microcontroller** with Wi-Fi  
- **3× SMPS units** for stable power supply  
- **RFID receiver + RFID cards**  
- **OLED display**  
- **MQ3 alcohol sensor**  
- **DHT11** for temperature & humidity  
- **Multiple sensors** for vibration/impact  
- **Buzzer** (alerts & indication)  
- **Camera** (captures barcodes & 3D shape of consignments)  

### 🔹 Protocols
- **MQTT Protocol** → Lightweight IoT data transmission  

### 🔹 Software & Blockchain
- **Hybrid Blockchain** (Public + Private)  
- **Data pipeline**: Hardware → MQTT → Blockchain storage  
- **Dashboard**: Displays real-time shipment health, location, and alerts  

---

## 🎥 Demo & Operation

### 1️⃣ Hardware Demo Setup
1. Place the **hardware module** inside a transport vehicle or warehouse.  
2. Sensors & CCTV continuously capture:  
   - Temperature & humidity (DHT11)  
   - Alcohol leaks or chemical presence (MQ3)  
   - Barcode & 3D package shape (Camera)  
   - Vibration/impact during transit (shock sensors)  
3. Data is processed by the **microcontroller** and sent via **Wi-Fi using MQTT**.  

### 2️⃣ Software Workflow
1. Real-time data from sensors is transmitted to the blockchain.  
2. **Public Blockchain** → Verifies that data is logged transparently.  
3. **Private Blockchain** → Provides secure access to authorized stakeholders.  
4. Dashboard visualizes shipment health, alerts, and location in real-time.  

### 3️⃣ Running the Demo
- **Step 1:** Connect the hardware to power (3× SMPS).  
- **Step 2:** Start the MQTT broker (e.g., Mosquitto).  
- **Step 3:** Launch the backend (Node.js/Express) to handle data.  
- **Step 4:** Start the blockchain environment (Ganache for testing / Hyperledger for deployment).  
- **Step 5:** Open the **React.js dashboard** → Monitor live shipment data.  

---

## 📊 Key Benefits
- 📦 **Quality Assurance** → Track environmental conditions to maintain product integrity.  
- ⚡ **Risk Management** → Detect spoilage, damage, or tampering in real-time.  
- 🛡️ **Counterfeit Prevention** → Verify authenticity through blockchain traceability.  

---

## 🚀 Future Scope
- AI/ML integration for **predictive spoilage detection**.  
- Integration with **GPS tracking** for smarter route optimization.  
- Expansion to **other sectors** like food, agriculture, and logistics.  

---

## 📂 Repository Structure
