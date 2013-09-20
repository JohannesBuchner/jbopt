Example code
=====================

See :doc:`doc` for which methods are available and how to call them.
::

	# define the problem:
	
	#   the log-likelihood function
	#   use a 5-dimensional gaussian likelihood surface
	centers = numpy.array([0.1, 15, 3.3, 4.1, 0])
	sigmas  = numpy.array([0.01, 0.1, 3, 10, 10])
	def loglikelihood(params):
		return -0.5 * (((params - centers) / sigmas)**2).sum()

	#   define the parameter space, in this case between -50 and +50
	#   also used in Bayesian methods for prior weighting
	def transform(cube):
		return numpy.asarray(cube) * 100 - 50

	#   define the prior weighting explicitly for some of the Bayesian methods
	#   in this case uniform between -50 and +50
	def prior(params):
		return 0
	
	from jbopt.classic import *
	from jbopt.mcmc import *
	from jbopt.mn import *
	from jbopt.de import *
	
	# the common parameters
	args = dict(
		loglikelihood=loglikelihood, transform=transform, prior=prior,
		parameter_names = ['c%d' % i for i in range(len(centers))],
		nsteps=2000, # maximum number of steps
		seed = 0,    # make output reproducible; set to -1 for random seed
		# disp = 1 # for more verbose output
	)
	
	# calling the various methods (common call interface)
	ret = classical(method='neldermead', **args)
	
	for method in 'cobyla', 'ralg', 'mma', 'auglag', 'minuit':
		print 'next method:', method
		ret = classical(method=method, **args)
	
	ret = onebyone(**args)
	ret = onebyone(parallel=True, find_uncertainties=True, **args)
	ret = de(output_basename='test_all_de', **args)
	ret = mcmc(output_basename='test_all_mcmc', **args)
	ret = ensemble(output_basename='test_all_mcmc', **args)
	ret = multinest(output_basename='test_all_mn', **args)
	
	# analyse a return value (common output interface)
	print ret['method'] # method used
	print ret['start']  # new ML value
	print ret['neval']  # number of evaluations used
	# not all methods provide also the following
	print ret['chain']  # Markov Chain, samples drawn from posterior
	print ret['median'] # medians of the parameters
	print ret['stdev']  # standard deviation uncertainty of the parameters


