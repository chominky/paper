p = -2.85
q = p/(1-p)
rho = 0.008
delta = 0.0004
transaction_cost = 0.03


def calculate_portfolio(mu_1=0.0001, mu_2=0.0052, sigma_1=0.0047, sigma_2=0.051):
    c_M = (1+q)*(delta - q/(2*(1-rho**2)) * ((mu_1/sigma_1)**2 + (mu_2/sigma_2)**2 - 2*rho*mu_1*mu_2/(sigma_1*sigma_2)))
    pi_1M = ((1+q)*(mu_1-rho*sigma_1*mu_2/sigma_2))/((1-rho**2)*sigma_1**2)
    pi_2M = (1+q)*(mu_2-rho*sigma_2*mu_1/sigma_1)/((1-rho**2)*sigma_2**2)

    print("Merton consumtion rate : {}".format(c_M))
    print("Merton illiquid asset ratio : {}".format(pi_1M))
    print("Merton liquid asset ratio : {}".format(pi_2M))

    eta = (3*(1+q)*(pi_1M**2)*((1-pi_1M)**2)/4 + 3*(1+q)*((mu_2*(1+q)-rho*sigma_1*sigma_2)**2)*(pi_1M)**2/(4*(1-rho**2)*(sigma_1**2)*(sigma_2**2)))**(1.0/3.0)
    x_lower = -q*pi_1M/c_M + q*eta*transaction_cost**(1.0/3.0)/c_M
    x_upper = -q*pi_1M/c_M - q*eta*transaction_cost**(1.0/3.0)/c_M
    g_lower = -1/c_M + q*(1-rho**2)*(sigma_1**2)*(eta**2)*transaction_cost**(2.0/3.0)/(2*(1+q)*c_M**2)
    g_upper = -1/c_M - q*(1-rho**2)*(sigma_1**2)*(eta**2)*transaction_cost**(2.0/3.0)/(2*(1+q)*c_M**2)

    pi_1M_lower = pi_1M - eta*transaction_cost**(1.0/3.0)
    pi_1M_upper = pi_1M + eta*transaction_cost**(1.0/3.0)
    pi_2M_lower = pi_2M - eta*sigma_1*rho*transaction_cost**(1.0/3.0)/sigma_2
    pi_2M_upper = pi_2M + eta*sigma_1*rho*transaction_cost**(1.0/3.0)/sigma_2
    c_hat = c_M - q*(1-rho**2)*(sigma_1**2)*(eta**2)*transaction_cost**(2.0/3.0)/(2*(1+q))

    print(pi_1M_lower)

    print("Optimal consumtion rate : {}".format(c_hat))
    print("{} <= Optimal illiquid asset ratio <= {}".format(pi_1M_lower, pi_1M_upper))
    print("{} <= Optimal liquid asset ratio <= {}".format(pi_2M_lower, pi_2M_upper))


if __name__ == "__main__":
    calculate_portfolio()