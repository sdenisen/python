Metabolite Annotation
​Mass spectrometry is a technique that can be used to detect the presence of metabolites (biochemical compounds) in a sample. In this technique, a neutral metabolite is ionized by gaining or losing a charged fragment (adduct), and then the mass-to-charge ratio is measured for this ionized metabolite. Your task is to annotate mass-spectrometry results: find for a measured mass-to-charge ratio from which metabolite it could come from.

Formally, there is a database of MM neutral metabolites with masses m_i > 0m
i
​
 >0 and a database of KK potential adducts with masses a_ia
i
​
  (a_ia
i
​
  can be both positive and negative). Then there are NN measured signals s_i > 0s
i
​
 >0. Each signal s_is
i
​
  corresponds to some metabolite m_jm
j
​
  (1 \le j \le M)(1≤j≤M) with an adduct a_ka
k
​
   (1 \le k \le K)(1≤k≤K) and some noise \DeltaΔ (can be both positive and negative), that is  s_i = m_j+a_k+\Deltas
i
​
 =m
j
​
 +a
k
​
 +Δ, with m_j+a_k > 0m
j
​
 +a
k
​
 >0.

Your task is to find for each of NN signals s_is
i
​
  the pair of metabolite m_jm
j
​
  and adduct a_ka
k
​
 with the closest sum m_j+a_km
j
​
 +a
k.


Input format
The first line of the input contains one integer TT (1 \leq T \leq 3)\,-(1≤T≤3)− the number of test cases.

Each test case is specified by four lines. The first line of each test case contains three integer numbers M, K, NM,K,N. The second line contains MM numbers m_i -m
i
​
 − masses of metabolites (0 < m_i\le 1000)(0<m
i
​
 ≤1000).  The third line contains KK numbers a_i -a
i
​
 − masses of adducts (-1000 \le a_i \le 1000)(−1000≤a
i
​
 ≤1000).  The fourth line contains NN numbers s_i -s
i
​
 − masses of signals (0 < s_i\le 1000)(0<s
i
​
 ≤1000). All the masses are indicated with exactly six decimal places.

Output format
For each signal s_is
i
​
  of each test case, print numbers jj and kk such that   s_i = m_j+a_k+\Deltas
i
​
 =m
j
​
 +a
k
​
 +Δ,  m_j+a_k > 0m
j
​
 +a
k
​
 >0 and an absolute value of \DeltaΔ is smallest possible. If there are multiple numbers jj and kk with same absolute value of \DeltaΔ for some signal, you can print any of them.