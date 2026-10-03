# JAGRUT-NETRA-AI-SURVEILLANCE-SYSTEM
Jagrut Netra is an AI-powered surveillance system for real-time security monitoring. Using OpenCV, Streamlit, and NumPy, it performs face detection and video analysis.

It supports crowd monitoring, fire/smoke detection, loitering detection, intrusion alerts, and night surveillance with real-time alerts and video recording.

**Main Monitoring Modules**

1.👥 Crowd Management

2.🔥 Fire & Smoke Detection

3.🚫 Restricted Area Security

4.🌙 Night-Time Surveillance

5.🚶 Loitering Detection

The system is designed to automate surveillance, provide real-time alerts, and support persistent video recording.

**🎯 Problem Statement**

Traditional surveillance systems often depend on continuous human monitoring of CCTV feeds. This can be time-consuming, prone to fatigue
and human error, and may delay the identification of abnormal events.

Jagrut Netra addresses this problem by applying artificial intelligence
and computer vision techniques to automatically analyze video inputs and
assist with real-time threat detection and monitoring.

**🎯 Objectives**

1.Develop real-time crowd monitoring using face detection and people counting.

2.Detect potential fire and smoke using HSV color-space-based segmentation.

3.Monitor restricted areas and identify unauthorized entry.

4.Provide surveillance capabilities for nighttime and low-light conditions.

5.Identify potential loitering by analyzing stationary or slow-moving behavior over time.

6.Provide real-time alerts and recording capabilities.

**🚀 Key Features**

👥 Crowd Management                 Detect faces and count people in a video frame

🔥 Fire & Smoke Detection           Identify potential fire/smoke regions

🚫 Restricted Area Security         Monitor protected areas for unauthorized entry

🌙 Night-Time Security              Monitor video feeds in low-light/night conditions

🚶 Loitering Detection              Analyze stationary or slow-moving behavior

🔔 Real-Time Alerts                 Trigger alerts when configured events are detected

🎥 Video Recording                  Save surveillance recordings when required

🌐 Streamlit Interface              Browser-based interface for selecting and controlling modules.

**🛠️ Technology Stack**

**Programming Language**:

  Python
  
**Computer Vision**:

OpenCV

Haar Cascade Classifiers

HSV Color-Space Segmentation

Video Frame Processing

**Data / Image Processing**:

NumPy

**Web Interface**:

Streamlit

**File & Video Handling**:

os

time

cv2.VideoWriter


**🏗️ System Architecture**

<img width="1180" height="1177" alt="image" src="https://github.com/user-attachments/assets/06e00211-f56d-4ac8-a744-fcf41ef91f87" />

**🔍 Modules**:

1. 👥 Crowd Management
   
2. 🔥 Fire & Smoke Detection
  
3. 🚫 Restricted Area Security
 
4. 🌙 Night-Time Surveillance
  
5. 🚶 Loitering Detection.

**🔔 Alert System**

The system can trigger an alert when a configured event is detected.

**Possible events include:**

Fire/smoke detection

Restricted-area intrusion

Loitering threshold exceeded

Other abnormal surveillance events

The project flow includes a sound alert using a beep/system sound with cooldown-based behavior.

**🎥 Video Recording**

Jagrut Netra supports recording of relevant surveillance activity.

**Video archival is handled using OpenCV's:**

cv2.VideoWriter

The system can save recordings when a selected surveillance section requires recording.

**📥 Input**

**The system is designed for video-based surveillance input, including:**

Camera feed

Video stream

Video frames

The exact supported input depends on the implementation in the project source code.

**📤 Output**

**Depending on the selected module, the system can provide:**

Detected face count

Fire/smoke highlighting

Restricted-area intrusion alerts

Night surveillance monitoring

Loitering alerts

Sound notifications

Saved video recordings

**▶️ How to Run**

streamlit run Project.py

**🌐 Application Interface**

<img width="995" height="906" alt="image" src="https://github.com/user-attachments/assets/0819920a-869e-45ee-ad69-ec5b4893196a" />

**💡 Use Cases**

**Jagrut Netra can be adapted for surveillance scenarios such as:**

**🏫 Educational Institutions**

Campus monitoring

Restricted-area monitoring

Crowd monitoring

**🏢 Organizations**

Office security

Entry monitoring

Restricted-zone surveillance

**🎪 Events**

Crowd monitoring

Overcrowding awareness

Fire/smoke monitoring

**🏙️ Public Areas**

Public-space monitoring

Suspicious-activity monitoring

Security assistance

**📈 Advantages**

Real-time video analysis

Automated surveillance

Multiple monitoring modules

Interactive web interface

Automated alerts

Video recording capability

Modular design

Reduced dependence on continuous manual monitoring

Potential scalability for multiple camera inputs

**⚠️ Limitations**

The project's documented limitation is that detection accuracy can be affected by low-resolution or poor-quality video feeds.

**Other practical factors that may affect results include:**

Lighting conditions

Camera positioning

Video quality

Detection thresholds

Computational resources

False positives and false negatives

**🔮 Future Enhancements**

**Possible future improvements include:**

**Multi-Camera Support**

Process multiple camera feeds simultaneously.

**Deep Learning Models**

Evaluate modern object-detection and tracking models.

**Improved Object Tracking**

Introduce more robust tracking for movement analysis.

**Notification Integration**

Add configurable notification channels for detected events.

**Centralized Dashboard**

Monitor multiple cameras and historical events from a single dashboard.

**Event Database**

Store event information such as timestamp, camera ID, event type, and recording path.

**Cloud Deployment**

Deploy the application and supporting services to a cloud environment.

**Performance Optimization**

Optimize frame processing and resource utilization for larger deployments.

**🧠 Learning Outcomes**

**This project provided practical experience in:**

Python application development

Computer Vision

OpenCV

NumPy

Image and video processing

Real-time frame analysis

Face detection

HSV-based image segmentation

Streamlit application development

Event detection

Alert mechanisms

Video recording

Modular software design

**🔐 Privacy & Responsible Use**

Jagrut Netra is an academic/prototype surveillance project intended for learning and experimentation.

**For real-world deployment, consider:**

Privacy regulations

Consent requirements

Data retention policies

Secure storage

Access control

Responsible handling of recorded footage

Human verification of automated detections

**📚 References**

**The project presentation references resources covering:**

Image processing with NumPy and OpenCV.

Face detection using OpenCV and Python.

Streamlit components and layouts.

**👨‍💻 Author**

Gudala Vamshi

Computer Science & Engineering Student

CMR College of Engineering & Technology, Hyderabad.
