cmake_minimum_required(VERSION 3.8) #minimum cmake version
project(task_one_interfaces)  #names the CMake project

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED) # loads the ros2 cmake build system

find_package(rosidl_default_generators REQUIRED) # loads the tool that generates ros2 message code from .msg file

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

#generate coresponding ros2 interface by taking the taskone.msg file in my msg directory
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/TaskOne.msg"
)

ament_export_dependencies(rosidl_default_runtime) # makes the runtime dependency available to packages using this interface

ament_package() # marks this as an ament ros2 package
