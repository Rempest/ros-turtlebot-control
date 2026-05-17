# Turtle Bot Control (ROS2)

Simple ROS2 Python package that publishes velocity commands to control a robot (e.g. TurtleSim or any robot listening to `/cmd_vel`).

---

## Package Information

**Name:** turtle_bot_control  
**Version:** 0.0.1  
**Author:** Raempest  
**Email:** thehuman130410@gmail.com  
**License:** MIT  
**Description:** Simple ROS2 node for controlling robot movement using Twist messages.

---
## Requirements

* **OS:** Ubuntu (or any Linux distribution officially supported by your ROS2 distro)
* **ROS2:** Compatible with Foxy, Humble, Iron, Jasmine, and newer distributions.
* **Build Tools:** `colcon`

---

## Setup and Installation

Before building the project for the first time, you must ensure that the directory structure is complete and create a required resource marker file.

### 1. Creating the Resource Marker (Required)
The `colcon` build system and `ament_python` build type require an empty marker file named exactly after your package inside the `resource` directory.

Open your terminal in the root folder of the project and run:
```bash
touch resource/turtle_bot_control
```
_Note: If you are using Windows or VS Code manually, simply create an empty file inside the resource folder named turtle_bot_control with no file extension._

##2. Workspace Setup and Compilation
_It is best practice to build your ROS2 packages inside a dedicated workspace (e.g., ros2_ws)._
   *1. Create the workspace structure and place your package inside the src folder:*
   ```bash
     mkdir -p ~/ros2_ws/src
     cd ~/ros2_ws/src
     # Clone or move your turtle_bot_control directory here
   ```
      Build the package using `colcon` from the workspace root:
  ```bash
   cd ~/ros2_ws
   colcon build --packages-select turtle_bot_control
   ```

