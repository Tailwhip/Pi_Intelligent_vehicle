#include "clamp.h"

double Clamp(float d, float min, float max) {
  const float t = d < min ? min : d;
  return t > max ? max : t;
}

