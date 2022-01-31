import numpy as np

def geo2helio(r_so,rhat_ob,d):
	"""
	Return the scalar multiplier for 'rhat_ob' that yields an 'r_so' of length 'd'
	NB: a=1 so we can omit it from calcs
	"""

	is_arr = isinstance(rhat_ob,np.ndarray) and rhat_ob.ndim==2

	if is_arr:
		b = 2*np.sum(r_so*rhat_ob,axis=1)
		c = -1*(d**2 - np.sum(r_so*r_so,axis=1))
	else:
		b = 2*np.dot(rhat_ob,r_so)
		c = -1*(d**2 - np.dot(r_so,r_so))

	s = np.sqrt(b**2 - 4*c)
	r0 = (-b + s)/2.0
	r1 = (-b - s)/2.0

	if is_arr:
		alpha = np.max(np.vstack((r0,r1)).T,axis=1)
		alpha[alpha<0] = np.nan
	else:
		alpha = np.max((r0,r1))
		if alpha<0:
			alpha = np.nan

	return alpha
