cmake_minimum_required(VERSION 3.8)

project(AOC2023)

set(SRC
	main.cpp
	stringParser.cpp
	day1.cpp
	day2.cpp
	)

set(HDR
	stringParser.hpp
	day1.hpp
	day2.hpp
	)
	
add_executable (AOC23 ${SRC} ${HDR})
