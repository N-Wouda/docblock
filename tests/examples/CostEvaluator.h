// Real-world example from PyVRP.

#ifndef PYVRP_COSTEVALUATOR_H
#define PYVRP_COSTEVALUATOR_H

#include "Measure.h"
#include "Solution.h"

namespace pyvrp
{
/**
 * Cost evaluator class that computes penalty values for timewarp and load.
 */
class CostEvaluator
{
    Cost capacityPenalty;
    Cost timeWarpPenalty;

public:
    CostEvaluator(Cost capacityPenalty, Cost timeWarpPenalty);

    /**
     * Computes the total excess capacity penalty for the given load.
     */
    [[nodiscard]] inline Cost loadPenalty(Load load, Load capacity) const;

    /**
     * Computes the excess capacity penalty for the given excess load, that is,
     * the part of the load that exceeds the capacity.
     */
    [[nodiscard]] inline Cost loadPenaltyExcess(Load excessLoad) const;

    /**
     * Computes the time warp penalty for the given time warp.
     */
    [[nodiscard]] inline Cost twPenalty(Duration timeWarp) const;

    /**
     * Computes a smoothed objective (penalised cost) for a given solution.
     */
    [[nodiscard]] Cost penalisedCost(Solution const &solution) const;

    /**
     * Computes the objective for a given solution. Returns the largest
     * representable cost value if the solution is infeasible.
     */
    [[nodiscard]] Cost cost(Solution const &solution) const;
};
}  // namespace pyvrp

#endif  // PYVRP_COSTEVALUATOR_H
