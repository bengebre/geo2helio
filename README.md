# geo2helio
Scale a geocentric observer-body unit vector to achieve the asserted length heliocentric vector to that body.  More details available <a href="https://benengebreth.org/dynamic-sky/geocentric-to-heliocentric/">here</a>.

#### Example usage

```python
from geo2helio import geo2helio

#inputs
r_so = np.array([1,0,0]) #sun->observer vector
rhat_ob = [0.5,0.5,0]/LA.norm([0.5,0.5,0]) #observer->body unit vector
d = 2 #distance guess

#call
alpha = geo2helio(r_so,rhat_ob,d)

#heliocentric vector magnitude
LA.norm(r_so + alpha*rhat_ob)

>> 2.0
```

#### You can also pass inputs as arrays for bulk calculations without a loop

```python
#inputs
r_so_arr = np.ones((3,3))*r_so
rhat_ob_arr = np.ones((3,3))*rhat_ob

#call
alpha = geo2helio(r_so_arr,rhat_ob_arr,d)

#heliocentric vector magnitudes
LA.norm(r_so + alpha*rhat_ob,axis=1)

>> array([2., 2., 2.])
```
