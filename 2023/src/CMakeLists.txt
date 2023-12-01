cmake_minimum_required(VERSION 3.8)

project(AOC2023)

set(SRC
	main.cpp
	day1.cpp
	)

set(HDR
	day1.hpp
	)
	
add_executable (AOC23 ${SRC} ${HDR})