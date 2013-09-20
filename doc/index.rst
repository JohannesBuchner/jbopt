=======================================
Welcome to jbopt's documentation!
=======================================

About
------------------------------

*jbopt* is a suite of powerful parameter space exploration methods.

Methods of likelihood maximization, estimation of uncertainty for parameter estimation
in a maximum likelihood and Bayesian way are available. 
The problem only has to be stated once, then the various methods can called 
interchangably, or in combination, by a common call interface (see the :doc:`code example<example>`).

Methods
---------

1. Optimization methods

 * :ref:`jbopt.classic<opt>`

  * **Nelder-Mead**, **COBYLA** (via `scipy.optimize <http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html>`_)
  * **ralg**, **auglag** and 100s others from the OpenOpt framework (via `openopt.NLP <http://openopt.org/NLP>`_)
  * **Minuit** (via `PyMinuit <https://code.google.com/p/pyminuit/>`_)
  * Custom minimization methods (see :ref:`here<1d>`)

 * :ref:`jbopt.de<de>`

  * **Differential evolution**, specially preconfigured (via `inspyred <http://inspyred.github.io/>`_)

2. Parameter estimation methods

 * :ref:`jbopt.mcmc<mcmc>`

  * **Metropolis Hastings MCMC** with automatic step width adaption
  * **Ensemble MCMC** (via `emcee <http://dan.iel.fm/emcee/>`_)

 * :ref:`jbopt.mn<mn>`

  * **MultiNest Nested Sampling** (via `PyMultiNest <http://johannesbuchner.github.com/PyMultiNest/index.html>`_)

3. Integration methods

 * see the `pymultinest/pycuba package <http://johannesbuchner.github.com/PyMultiNest/index.html>`_

Documentation
-------------------------------

.. toctree::
	example
	doc
	:maxdepth: -1


Installation
-------------------------------

#. using pip::

	$ pip install jbopt # also consider the --user option

#. Get source using git: *jbopt* is hosted at `https://github.com/JohannesBuchner/jbopt<https://github.com/JohannesBuchner/jbopt>`_
	::

	$ git clone git://github.com/JohannesBuchner/jbopt
	$ cd jbopt
	$ python setup.py install # also consider the --user option

Be aware that you will have to install the various dependencies for the 
algorithms you would like to use.

Indices and tables
-------------------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

