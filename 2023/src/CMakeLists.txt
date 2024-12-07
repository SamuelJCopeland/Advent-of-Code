cmake_minimum_required(VERSION 3.8)

project(AOC2023)

set(SRC
	main.cpp
	stringParser.cpp
	day1.cpp
	day2.cpp
	day3.cpp
	day4.cpp
	day5.cpp
	)

set(HDR
	stringParser.hpp
	day1.hpp
	day2.hpp
	day3.hpp
	day4.hpp
	day5.hpp
	)
	
add_executable (AOC23 ${SRC} ${HDR})
