// Another example from PyVRP, featuring documentation with significant
// whitespace. Documentation snipped for brevity.

#ifndef PYVRP_DIVERSITY_H
#define PYVRP_DIVERSITY_H

#include "ProblemData.h"
#include "Solution.h"

#include <functional>

namespace pyvrp::diversity
{
typedef std::function<double(Solution const &, Solution const &)>
    DiversityMeasure;

/**
 * Parameters
 * ----------
 * first
 *     First solution.
 * second
 *     Second solution.
 */
double brokenPairsDistance(Solution const &first, Solution const &second);
}  // namespace pyvrp::diversity

#endif  // PYVRP_DIVERSITY_H
