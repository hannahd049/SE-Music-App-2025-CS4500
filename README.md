# Software Requirements Specification (SRS)
## Project: **Hit or Miss** (Music Tinder)
## Course: CS 4500 – Risks and Requirements

### Produced By
- Allen, Chase  
- Cogoli, Sara  
- Dees, Hannah  
- Green, Emma  
- Malomboza, Zimani  
- Maurer, Issac  
- Onyekachi, Ekene “E.J.”  
- Siegler, Patrick  
- Wolfe, Kyra I  

### Document Prepared By  
**Ekene “E.J.” Onyekachi**

---

# 1. Introduction

## 1.1 Purpose
The purpose of this SRS document is to define the requirements, features, risks, and constraints of the **Hit or Miss** music-discovery application. The document is intended for developers, testers, and project stakeholders.

## 1.2 Scope
**Hit or Miss** is a music-browsing application that plays short clips of songs and allows users to vote “YAY” or “NAY.” Based on user interactions, the system recommends new songs and stores liked tracks in customizable playlists. The application also displays usage statistics to enhance user engagement.

## 1.3 Definitions and Acronyms
- **YAY/NAY** – Binary voting mechanism for song preference  
- **Playlist** – A user-defined collection of liked songs  
- **Clip** – A 5–30 second preview of a track  
- **API** – External service used for retrieving songs and metadata  

---

# 2. Overall Description

## 2.1 Product Perspective
The application acts as a music-recommendation tool similar to a swipe-based discovery interface, using short audio previews and user voting behavior to determine preferences.

## 2.2 User Classes and Characteristics
- **General Users** – Standard users interacting with music previews and playlists  
- **Music Enthusiasts** – Users interested in statistics and detailed music metadata  

*Note: Application requires that users be able to hear audio previews.*

## 2.3 Operating Environment
The system will run on any modern device capable of:
- Audio playback  
- Touch or mouse input  
- Internet connectivity (to access music API)  

---

# 3. System Features

## 3.1 Song Preview
**Description:**  
- Play an initial 5–10 second clip of a song  
- Allow replay and expansion up to 30 seconds  

**Requirements:**  
- The system shall play audio clips reliably.  
- The system shall allow replay of a clip up to 30 seconds.  

## 3.2 Voting System
**Description:**  
Users vote **YAY** or **NAY** on each song.

**Requirements:**  
- The system shall record the user’s vote for each song.  
- The system shall use these votes to influence future song recommendations.  

## 3.3 Playlist Management
**Description:**  
Liked songs are added automatically to a playlist, and users can sort or categorize them.

**Requirements:**  
- The system shall add YAY-voted songs to a playlist.  
- The system shall allow users to organize songs into multiple playlists.  

## 3.4 Song Metadata Display
**Includes:**  
- Title  
- Artist  
- Year  
- Genre  
- Mood  

**Requirements:**  
- The system shall display metadata for each song played.  

## 3.5 Statistics Tracking
**Description:**  
The application provides basic analytics on user preferences.

**Examples:**  
- “How many pop songs have you liked?”  
- “You liked # songs from the 80s.”  

**Requirements:**  
- The system shall generate statistics based on likes/dislikes.  

---

# 4. External Requirements

## 4.1 System Requirements
- UI elements must respond to clicks/taps.  
- The system must be able to switch songs and playback smoothly.  
- The system shall display a start screen.  
- Liked songs must be saved persistently.

## 4.2 User Requirements
- Must use a device capable of audio playback.  
- Must be able to interact with the interface manually.  
- Basic decision-making required.  
- *Users cannot be deaf; no captions or alternative accessibility options are included.*  

---

# 5. Risks and Mitigations

## 5.1 Technical Risk: API May Execute Twice  
**Mitigation:** Implement a **singleton pattern** to prevent redundant initialization or calls.

## 5.2 Legal Risk: Use of Original Song Material  
**Mitigation:** Limit playback to **30-second previews**, aligning with typical licensing and fair-use restrictions.

---

# 6. Conclusion
This SRS outlines the structure and requirements necessary to build the **Hit or Miss** music discovery application. By adhering to these specifications, developers can ensure functionality, consistency, and user engagement throughout the system.
