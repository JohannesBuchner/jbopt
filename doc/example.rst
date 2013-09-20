Example code
=====================

First, lets define the problem.

We will use the **log-likelihood function** of a 5-dimensional gaussian likelihood surface::

	centers = numpy.array([0.1, 15, 3.3, 4.1, 0])
	sigmas  = numpy.array([0.01, 0.1, 3, 10, 10])

        def loglikelihood(params):
	        return -0.5 * (((params - centers) / sigmas)**2).sum()

Next, we define the **parameter space**, in this case between -50 and +50.
This function is also used in Bayesian methods for prior weighting::

	def transform(cube):
		return numpy.asarray(cube) * 100 - 50

We also define the **prior weighting** explicitly for some of the Bayesian methods;
Other methods will not use it. Again, in this case we consider a uniform prior::

	def prior(params):
		return 0

Some imports::

	from jbopt.classic import *
	from jbopt.mcmc import *
	from jbopt.mn import *
	from jbopt.de import *

All methods have arguments in common, namely the loglikelihood, transform and prior
defined above. Also, the maximum number of steps is obeyed by most algorithms.
So lets define the common arguments for re-use::

        # the common parameters
	args = dict(
		loglikelihood=loglikelihood, transform=transform, prior=prior,
		parameter_names = ['c%d' % i for i in range(len(centers))],
		nsteps=2000, # maximum number of likelihood evaluations
                # start = [0.5, 0.3, 0.5, 0.7, 0.9], # set starting point
		# seed = 0,  # set for reproducible output
		# disp = 1,  # for more verbose output
	)

Now we **call the various methods**, starting with the simple Nelder-Mead.
See :doc:`doc` for which methods are available and how to call them::

	ret = classical(method='neldermead', **args)

Minuit, COBYLA and some methods through OpenOpt::

	for method in 'cobyla', 'ralg', 'mma', 'auglag', 'minuit':
		print 'next method:', method
		ret = classical(method=method, **args)

A custom algorithm::

	ret = onebyone(**args)
	ret = onebyone(parallel=True, find_uncertainties=True, **args)

Differential evolution, MCMC, Ensemble MCMC and MultiNest::

	ret = de(output_basename='test_all_de', **args)
	ret = mcmc(output_basename='test_all_mcmc', **args)
	ret = ensemble(output_basename='test_all_mcmc', **args)
	ret = multinest(output_basename='test_all_mn', **args)

For each, we can analyse the return value, which gives information about what was
learned about the parameter space. This of course varies between the methods::

	print ret['method'] # method used
	print ret['start']  # new maximum likelihood value
	print ret['neval']  # number of evaluations used
	# some methods also provide the following
	print ret['chain']  # Markov Chain, samples drawn from posterior
	print ret['median'] # medians of the parameters
	print ret['stdev']  # standard deviation uncertainty of the parameters

Read more in the :doc:`doc`.
