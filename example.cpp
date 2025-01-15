#include "gtest/gtest.h"

#include <string>

TEST(arithmetic, add) {
    ASSERT_EQ(1, 2 + -1);
}

TEST(string, add) {
    ASSERT_EQ("hello, world", std::string("hello, ") + "world");
}
