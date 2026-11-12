# Software FJ - Object-Oriented Management System

## Overview
This repository contains the collaborative software solution developed as a response to the practical problem statement and requirements defined for Phase 4. The project implements an object-oriented system for managing customers, specialized services (event rooms, equipment, and consulting), and reservations without using a database, relying strictly on in-memory lists, object structures, and advanced exception handling with automated logging.

* **Problem Statement Reference:** ([View the Problem Description PDF Link Here](https://1drv.ms/b/c/80422ad77e43d596/IQDYwO_NtHmYTI2o5F9_LnLrAaFwPxtvwvtQPqSUOShhBDg?e=4s31BD))

---

## System Architecture & UML Design
To establish a clear structural blueprint for the team, the object-oriented architecture includes abstract classes, inheritance, encapsulation, method overriding, and method overloading.

* **UML Class Diagram:** ([View the Interactive/Visual UML Diagram Here](https://drive.google.com/file/d/1tW3dHyLlpzR33P0932_VnBJrT3RV8O7e/view?usp=sharing))

* **Decision & Process Flow:** ([View the System Decision Flowchart Here](https://drive.google.com/file/d/1w98Lkfg9Wg-xct7AOlHH4JBejuy7VuSw/view?usp=sharing))

---

## Project Consolidation & Final Delivery
All individual components, modular scripts, version-controlled features, and execution files have been fully consolidated directly within this GitHub repository. Furthermore, the complete technical development have been consolidated in the next document:

* **Consolidation document:** ([View the Consolidation document .DOC Link Here](https://unadvirtualedu-my.sharepoint.com/:w:/g/personal/jkgalviss_unadvirtual_edu_co/IQDXgr3vUsatQofiY_nWD6gRARwOgkMZAwAv6JM123WXfbo?e=0ByHNq))

---

## Development Structure & Team Contributions

The project was systematically developed and modularized into **5 core blocks** with collaborative contributions from the team members:

* **Block 1 (JGalvisS):**
  * Implementation of the `Customer` class with strict data encapsulation and input validations.
  * Creation of the custom exception classes (`Exception_System`, `Error_Invalid_Client`, `Service_Not_Available_Exception`, `Exception_customer`).
  * Initialization of the `Reservations` class focusing on the constructor and the `create_customer` method.

* **Block 2 (duverjr11-cmyk):**
  * Development of the abstract base class `Service`.
  * Implementation of specialized subclasses (`Event_room`, `Equipment`, `Consulting`) incorporating polymorphism, method overriding, and simulated method overloading for cost calculations.

* **Block 3 (AngelloWTFpy):**
  * Expansion of the `Reservations` class to handle core booking logic.
  * Implementation of methods for availability validation (`available_validate`), event room reservations (`event_room_reserve`), equipment rentals (`equipment_reserve`), and specialized consulting bookings (`consulting_reserve`).

* **Block 4 (Team Collaboration):**
  * Development of the remaining reservation functions and management routines.
  * Formatting internal lists into clean, readable text strings (`pretty print`) for enhanced user experience and clear console outputs.

* **Block 5 (Final Integration & Documentation):**
  * Development of the `main.py` entry point featuring an interactive, clean console-based user interface with structured inputs.
  * Comprehensive logging configuration (`sistema_software_fj.log`) tracking system events, warnings, and errors.

---

## Project Structure
* `main.py`: Application entry point, logging configuration, and simulation of operations.
* `Customer.py`: Customer management class with strict data encapsulation and validation.
* `Service.py`: Abstract base class `Service` and specialized subclasses (`Event_room`, `Equipment`, `Consulting`) implementing polymorphism and method overloading.
* `Reservation.py`: Controller class integrating customers and services with robust `try/except/else/finally` exception blocks and error chaining.
* `Exception.py`: Custom exception classes inheriting from Python's base `Exception`.
* `sistema_software_fj.log`: Automatically generated log file tracking system events and errors.

---

## Prerequisites & Requirements
* Python 3.8 or higher installed on your local machine.
* No external database engines or complex third-party libraries are required (uses standard Python libraries such as `logging`, `re`, and `datetime`).

---

## How to Run the Project

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/JGalvisS/pragramacion_fase_4_unad.git](https://github.com/JGalvisS/pragramacion_fase_4_unad.git)
   cd [pragramacion_fase_4_unad]

2. **Execute the application:**
   Run the main script from your terminal or IDE:
   ```bash
   python main.py
   ```

3. **Check the Logs:**
   After execution, verify that the `sistema_software_fj.log` file has been automatically created in the root directory.