// BC1 / BC2 / BC3 block → ASTC 4x4 LDR block (16 bytes), integer only.
#pragma once
#include <stdint.h>
typedef uint32_t u32; typedef int32_t s32; typedef int64_t s64; typedef uint64_t u64; typedef uint8_t u8;
#define BCA_FN static inline
#define BCA_T
#define BCA_K static const
#define BCA_BODY(...) __VA_ARGS__
#include "bc2astc_body.inc"
#undef BCA_BODY