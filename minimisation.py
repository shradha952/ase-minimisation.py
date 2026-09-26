def weighted_alternating_simulation_minimization(S, delta_s, delta_w):
    """
    Computes the maximal weighted alternating simulation relation, equivalence classes, 
    and builds the reduced transition system.
    
    Parameters:
    - S: list or set of states
    - delta_s: set of system moves represented as tuples (p, p_prime, w)
    - delta_w: set of world moves represented as tuples (p, p_prime, w)
    
    Returns:
    - R: Simulation relation set of pairs (p, q)
    - C: List of equivalence classes (sets of states)
    - (hat_S, hat_delta_s, hat_delta_w): The reduced system tuple
    """
    # Step 1: Compute Simulation Relation R
    R = {(p, q) for p in S for q in S}
    
    changed = True
    while changed:
        r_next = set()
        for p, q in R:
            # system_ok condition: 
            # \forall (p, p', w_p) \in \Delta_s, \exists (q, q', w_q) \in \Delta_s s.t. w_q \le w_p \land (p', q') \in R
            system_ok = True
            p_transitions = [t for t in delta_s if t[0] == p]
            q_transitions = [t for t in delta_s if t[0] == q]
            
            for p_trans in p_transitions:
                _, p_prime, w_p = p_trans
                found_match = False
                for q_trans in q_transitions:
                    _, q_prime, w_q = q_trans
                    if w_q <= w_p and (p_prime, q_prime) in R:
                        found_match = True
                        break
                if not found_match:
                    system_ok = False
                    break
            
            # world_ok condition: 
            # \forall (q, q', w_q) \in \Delta_w, \exists (p, p', w_p) \in \Delta_w s.t. w_p \ge w_q \land (p', q') \in R
            world_ok = True
            p_w_transitions = [t for t in delta_w if t[0] == p]
            q_w_transitions = [t for t in delta_w if t[0] == q]
            
            for q_trans in q_w_transitions:
                _, q_prime, w_q = q_trans
                found_match = False
                for p_trans in p_w_transitions:
                    _, p_prime, w_p = p_trans
                    if w_p >= w_q and (p_prime, q_prime) in R:
                        found_match = True
                        break
                if not found_match:
                    world_ok = False
                    break
            
            if system_ok and world_ok:
                r_next.add((p, q))
                
        changed = (R != r_next)
        R = r_next

    # Step 2: Compute Equivalence Classes
    C = []
    visited = set()
    
    def get_repr(class_set):
        # Select a deterministic representative from the equivalence class
        return sorted(list(class_set), key=str)[0]

    def find_rep(state, classes):
        for c in classes:
            if state in c:
                return get_repr(c)
        return state

    for p in S:
        if p not in visited:
            class_p = {q for q in S if (p, q) in R and (q, p) in R}
            C.append(class_p)
            visited.update(class_p)

    # Step 3: Build Reduced System
    hat_S = {get_repr(c) for c in C}
    hat_delta_s = set()
    hat_delta_w = set()
    
    for c in C:
        u = get_repr(c)
        for p in c:
            # Map system transitions
            for trans in delta_s:
                if trans[0] == p:
                    _, p_prime, w = trans
                    p_prime_rep = find_rep(p_prime, C)
                    hat_delta_s.add((u, p_prime_rep, w))
            # Map world transitions
            for trans in delta_w:
                if trans[0] == p:
                    _, p_prime, w = trans
                    p_prime_rep = find_rep(p_prime, C)
                    hat_delta_w.add((u, p_prime_rep, w))
                    
    return R, C, (hat_S, hat_delta_s, hat_delta_w)