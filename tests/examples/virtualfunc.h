// Small example of a virtual function with a default implementation directly
// inside the class declaration.

class Callbacks
{
    /**
     * Called at search start.
     */
    virtual void onStart(Solution const &initial){};
};
