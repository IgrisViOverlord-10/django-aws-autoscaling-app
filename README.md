# 🚀 Scalable Django Deployment on AWS with ALB & Auto Scaling

## 📌 Project Overview
Designed and deployed a dynamic Django web application using a scalable AWS architecture with load balancing and auto scaling to ensure high availability and fault tolerance.

---

## ❓ Why This Approach?
- Handles traffic efficiently using load balancing  
- Ensures high availability with multiple EC2 instances  
- Automatically replaces unhealthy instances  
- Reflects real-world production deployment practices  

---

## 💻 Tech Stack
AWS EC2, Application Load Balancer (ALB), Auto Scaling Group (ASG), Nginx, Gunicorn, Django

---

## 🏗 Architecture Flow
Client → ALB → EC2 (Auto Scaling) → Nginx → Gunicorn → Django → Response

---

## ⚙️ Implementation Summary
- Launched EC2 instance and deployed Django application  
- Configured Gunicorn as application server  
- Set up Nginx as reverse proxy  
- Created AMI from configured instance  
- Built Launch Template using AMI  
- Configured Target Group with health checks  
- Deployed Application Load Balancer  
- Created Auto Scaling Group with multiple instances  

---

## 🛠 Implementation Steps
1. Launch EC2 instance and install dependencies  
2. Deploy Django application  
3. Configure Gunicorn and test application  
4. Setup Nginx reverse proxy  
5. Create AMI from configured instance  
6. Create Launch Template using AMI  
7. Setup Target Group and health checks  
8. Create Application Load Balancer  
9. Configure Auto Scaling Group  
10. Validate traffic routing and instance health  

---

## 🔐 Security & Considerations
- EC2 instances allow HTTP and restricted SSH access  
- Application runs behind ALB (no direct dependency on single instance)  
- Health checks ensure only healthy instances receive traffic  
- Limitation: Gunicorn started manually (no process manager used)  

---

## 🚀 Key Outcomes
- Successfully deployed a dynamic Django application on AWS  
- Implemented load balancing across multiple instances  
- Achieved fault tolerance using Auto Scaling Group  
- Transitioned from static hosting to scalable architecture  

---

## 📂 Repository Files
calculator/ – Django app logic  
calculator_project/ – Project configuration  
templates/ – Frontend UI  
manage.py – Django entry point  
README.md – Project documentation  

---

## 📸 Snapshots Include
- Application running via ALB DNS  
- Target Group health status (multiple healthy instances)  
- AWS architecture diagram  

---

## 🎥 Recording
Recording attached showcasing the Django application running via the ALB endpoint.

---

## 💡 Conclusion
This project demonstrates how modern applications are deployed with scalability, load balancing, and high availability using AWS services.

---
