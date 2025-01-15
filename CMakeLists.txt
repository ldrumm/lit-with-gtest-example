project(lit-gtest)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/5376968f6948923e2411081fd9372e71a59d8e77.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# Now simply link against gtest or gtest_main as needed. Eg
add_executable(example.test example.cpp)
target_link_libraries(example.test gtest_main)

add_custom_target(
  check-lit
  COMMENT "Running lit tests"
  COMMAND lit ${CMAKE_SOURCE_DIR} -sv -DCMAKE_BINARY_DIR=${CMAKE_BINARY_DIR}
  DEPENDS example.test
  USES_TERMINAL
)
