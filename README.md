# 🌐 Network Monitoring System

<div align="center">

![Network Monitor](generated-icon.png)

*A comprehensive real-time network monitoring and analysis system built with modern web technologies*

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![React](https://img.shields.io/badge/React-18+-61DAFB.svg)](https://reactjs.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.42+-FF4B4B.svg)](https://streamlit.io)
[![Node.js](https://img.shields.io/badge/Node.js-Latest-339933.svg)](https://nodejs.org)
[![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1.svg)](https://mysql.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[🚀 Demo](#demo) • [📖 Documentation](#documentation) • [🛠️ Installation](#installation) • [🎯 Features](#features)

</div>

---

## 📋 Table of Contents

- [🎯 Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [🛠️ Installation](#️-installation)
- [🚀 Quick Start](#-quick-start)
- [💻 Usage](#-usage)
- [🔧 Tech Stack](#-tech-stack)
- [📸 Screenshots](#-screenshots)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 🎯 Features

### 🔍 **Real-Time Network Monitoring**
- **Live Traffic Analysis**: Monitor network packets in real-time with advanced filtering
- **Performance Metrics**: Track download/upload speeds, ping times, and latency
- **Interface Monitoring**: Support for multiple network interfaces (Ethernet, WiFi, etc.)

### 🛡️ **Security & Threat Detection**
- **Suspicious Pattern Detection**: Identify potential malware and attack signatures
- **Packet Classification**: Analyze captured packets for security threats
- **Alert System**: Real-time notifications for suspicious network activity

### 📊 **Interactive Dashboards**
- **Multiple Visualization Libraries**: Powered by Plotly, Nivo, and Recharts
- **Traffic Heatmaps**: Visual representation of network traffic patterns
- **Network Topology Maps**: Interactive network mapping and visualization
- **Historical Data**: Track and analyze network performance over time

### ⚡ **Real-Time Communication**
- **WebSocket Integration**: Live data updates using Socket.IO
- **Multi-Client Support**: Simultaneous monitoring from multiple dashboards
- **Event-Driven Architecture**: Efficient real-time data streaming

## 🏗️ Architecture

This system features a **hybrid architecture** combining the best of both Python and JavaScript ecosystems:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React Frontend │    │  Streamlit App  │    │   Express API   │
│   (Port 3002)    │◄──►│   (Port 5000)   │◄──►│   (Port 3001)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                        │                        │
         └────────────────────────┼────────────────────────┘
                                  │
                         ┌─────────────────┐
                         │  MySQL Database │
                         │   + SQLAlchemy  │
                         └─────────────────┘
```

### 🔧 **Core Components**

- **Frontend Layer**: React with Material-UI for modern, responsive interfaces
- **Analysis Engine**: Python backend with Streamlit for rapid prototyping
- **API Gateway**: Express.js server handling REST APIs and WebSocket connections
- **Data Layer**: MySQL database with SQLAlchemy ORM for robust data management
- **Network Engine**: Scapy for packet capture and analysis

## 🛠️ Installation

### Prerequisites

Make sure you have the following installed:

- **Python 3.11+**
- **Node.js 18+** 
- **MySQL 8.0+**
- **Git**

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/network-monitoring-system.git
cd network-monitoring-system
```

### 2. Backend Setup (Python)

```bash
# Install Python dependencies
pip install -r requirements.txt

# Alternative: Use uv for faster installs
uv sync
```

### 3. Frontend Setup (Node.js)

```bash
# Install Node.js dependencies
npm install

# Or use yarn
yarn install
```

### 4. Database Setup

```bash
# Setup database (ensure MySQL is running)
python -c "from models import create_tables; create_tables()"
```

### 5. Environment Configuration

Create a `.env` file with your database credentials:

```env
DATABASE_URL=mysql://username:password@localhost/network_monitor
MYSQL_HOST=localhost
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=network_monitor
```

## 🚀 Quick Start

### Option 1: Development Mode (All Services)

```bash
# Terminal 1: Start the Streamlit app
streamlit run main.py --server.port 5000

# Terminal 2: Start the Express API server
node server/index.js

# Terminal 3: Start the React frontend
npm run dev
```

### Option 2: Using Process Manager

```bash
# Install PM2 globally
npm install -g pm2

# Start all services
pm2 start ecosystem.config.js
```

### 🌐 **Access Points**

- **Streamlit Dashboard**: http://localhost:5000
- **React Frontend**: http://localhost:3002  
- **API Server**: http://localhost:3001/api

## 💻 Usage

### 🖥️ **Streamlit Dashboard**

The main monitoring interface provides:

1. **Network Performance Metrics**
   - Real-time speed tests
   - Ping measurements
   - Interface statistics

2. **Packet Analysis**
   - Live packet capture
   - Protocol analysis
   - Suspicious activity detection

3. **Alert Management**
   - Security notifications
   - Performance warnings
   - System status updates

### ⚛️ **React Frontend**

Modern web interface featuring:

- **Dashboard**: Overview of all network metrics
- **Packet Analysis**: Detailed packet inspection tools
- **Network Map**: Visual network topology
- **Alerts**: Centralized notification system

### 🔧 **API Endpoints**

```bash
GET /api/network/interfaces     # List network interfaces
GET /api/metrics/latest        # Get recent performance data
GET /api/packets/suspicious    # Retrieve flagged packets
POST /api/alerts/acknowledge   # Mark alerts as seen
```

## 🔧 Tech Stack

### **Frontend Technologies**
| Technology | Purpose | Version |
|------------|---------|---------|
| ![React](https://img.shields.io/badge/-React-61DAFB?style=flat&logo=react&logoColor=white) | UI Framework | 18.2+ |
| ![Material-UI](https://img.shields.io/badge/-Material--UI-0081CB?style=flat&logo=mui&logoColor=white) | Component Library | 5.14+ |
| ![Vite](https://img.shields.io/badge/-Vite-646CFF?style=flat&logo=vite&logoColor=white) | Build Tool | 6.1+ |
| ![Socket.IO](https://img.shields.io/badge/-Socket.IO-010101?style=flat&logo=socket.io&logoColor=white) | Real-time Communication | 4.7+ |

### **Backend Technologies**
| Technology | Purpose | Version |
|------------|---------|---------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) | Core Backend | 3.11+ |
| ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) | Web App Framework | 1.42+ |
| ![Node.js](https://img.shields.io/badge/-Node.js-339933?style=flat&logo=node.js&logoColor=white) | API Server | Latest |
| ![Express](https://img.shields.io/badge/-Express-000000?style=flat&logo=express&logoColor=white) | Web Framework | 4.21+ |

### **Data & Analysis**
| Technology | Purpose | Version |
|------------|---------|---------|
| ![MySQL](https://img.shields.io/badge/-MySQL-4479A1?style=flat&logo=mysql&logoColor=white) | Database | 8.0+ |
| ![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-D71F00?style=flat&logo=sqlalchemy&logoColor=white) | ORM | 2.0+ |
| ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat&logo=pandas&logoColor=white) | Data Analysis | 2.2+ |
| ![Plotly](https://img.shields.io/badge/-Plotly-3F4F75?style=flat&logo=plotly&logoColor=white) | Visualization | 6.0+ |

### **Network Analysis**
| Technology | Purpose | Version |
|------------|---------|---------|
| ![Scapy](https://img.shields.io/badge/-Scapy-2C3E50?style=flat) | Packet Capture | 2.6+ |
| ![psutil](https://img.shields.io/badge/-psutil-0078D4?style=flat) | System Monitoring | 7.0+ |
| speedtest-cli | Network Speed Testing | 2.1+ |

## 📸 Screenshots

<div align="center">

### 🖥️ Main Dashboard
*Real-time network monitoring with performance metrics*

### 📊 Packet Analysis
*Live packet capture and suspicious activity detection*

### 🗺️ Network Topology
*Interactive network mapping and traffic visualization*

### 🚨 Security Alerts
*Centralized alert management system*

</div>

> 📁 More screenshots available in `/documentation/screenshots/`

## 🚀 Deployment

### Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up -d
```

### Production Deployment

```bash
# Build React frontend
npm run build

# Start production servers
NODE_ENV=production node server/index.js
streamlit run main.py --server.headless true --server.port 5000
```

## 🧪 Testing

```bash
# Run Python tests
python -m pytest tests/

# Run JavaScript tests
npm test

# Run integration tests
npm run test:integration
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### 🔄 Development Workflow

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### 🐛 Bug Reports

Found a bug? Please open an issue with:
- **Description** of the problem
- **Steps** to reproduce
- **Expected** vs **actual** behavior
- **Environment** details (OS, Python version, etc.)

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with ❤️ using React, Python, and modern web technologies**

[⭐ Star this repository](https://github.com/yourusername/network-monitoring-system) if you found it helpful!

</div>
