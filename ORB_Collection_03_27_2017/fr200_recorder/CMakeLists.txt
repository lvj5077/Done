cmake_minimum_required(VERSION 2.8)

project(fr200_recorder)


find_package(OpenCV 3.0 REQUIRED) 
include_directories(
  ${OpenCV_INCLUDE_DIRS}
)

message("OPENCV_INCLUDE_DIRS ${OpenCV_INCLUDE_DIRS}")

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  message_filters
  cv_bridge
  image_transport
  tf
)

catkin_package(
  CATKIN_DEPENDS roscpp std_msgs tf
  DEPENDS std_msgs opencv 
)

SET( CMAKE_CXX_COMPILER "g++")
SET( CMAKE_BUILD_TYPE Release )
SET( CMAKE_CXX_FLAGS "-O3 -std=c++11" )


include_directories(
  ${catkin_INCLUDE_DIRS}
)

# add_executable(saveRGBD src/saveRGBD.cpp)
# target_link_libraries(saveRGBD ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})

message("OpenCV_LIBRARIES: ${OpenCV_LIBRARIES}")
add_executable(saveRGBD_orb src/saveRGBD_orb.cpp)
target_link_libraries(saveRGBD_orb ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})


# add_executable(saveRGBD_orb_reg src/saveRGBD_orb_reg.cpp)
# target_link_libraries(saveRGBD_orb ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})
