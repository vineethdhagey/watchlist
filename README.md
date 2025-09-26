# 🎬 Watchlist Application (Microservices + Kubernetes)
This project is a **microservice-based application** built with **Python Flask**, **MongoDB**, and deployed on **Kubernetes (Minikube)**.  
The system allows users to **register, log in, and manage their movie watchlist** with persistent storage.  

---

## 🚀 Features
- **User Authentication** – Register, Login, Logout (Auth-Service).  
- **Movie Management** – Add and fetch movies linked to a user (Movie-Service).  
- **Persistent Database** – MongoDB with PersistentVolumeClaim ensures data is not lost when pods restart.  
- **Kubernetes Deployment** – Each service runs in its own pod with service discovery and scaling support.  
- **Frontend Integration** – `index.html` served by Auth-Service acts as the UI for the whole system.

---

## 🏗️ Architecture Overview
- **Auth-Service (Flask + Frontend)**  
  Handles `/register`, `/login`, `/logout`, and serves the frontend.  
- **Movie-Service (Flask)**  
  Handles `/api/add_movie` and `/api/movies/{user_id}`.  
- **MongoDB**  
  Stores user and movie data persistently.  
- **Kubernetes Services**  
  Internal routing between services and external NodePort for browser access.

  
---

## ⚙️ Setup & Deployment Instructions

### 1. Clone Repository
```bash
git clone https://github.com/vineethdhagey/watchlist.git
cd watchlist

```
### 2. Start Minikube
```bash
minikube start

```

### 3. Deploy Application
```bash
kubectl apply -f watchlist-deployment.yaml

```
### 4. Verify Pods & Services
```bash
kubectl get pods -n watchlist-app
kubectl get svc -n watchlist-app

```
### 5. Access Application
```bash
minikube service auth-service -n watchlist-app

```
This will open the browser with the frontend UI.

## 🌐 API Endpoints
### Auth-Service
- **POST /register** → Register a new user

- **POST /login** → Login

- **POST /logout** → Logout

### Movie-Service
- **POST /api/add_movie** → Add a movie for the logged-in user

- **GET /api/movies/{user_id}** → Fetch movies for a specific user



