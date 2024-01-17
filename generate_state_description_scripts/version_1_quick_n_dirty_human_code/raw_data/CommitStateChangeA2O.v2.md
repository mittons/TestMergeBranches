### Commit A (on main)
- **main**: 
  - History: `A`
  - Data: `A`
- **staging**: 
  - History: ` `
  - Data: ` `

### Checkout A (to staging, from main branch)
- **main**: 
  - History: `A`
  - Data: `A`
- **staging**: 
  - History: ` `
  - Data: `A`

### Commit B (on staging)
- **main**: 
  - History: `A`
  - Data: `A`
- **staging**: 
  - History: `B`
  - Data: `A, B`

### Commit C (on staging)
- **main**: 
  - History: `A`
  - Data: `A`
- **staging**: 
  - History: `B, C`
  - Data: `A, B, C (includes createdir.sh)`

### Commit D (on staging)
- **main**: 
  - History: `A`
  - Data: `A`
- **staging**: 
  - History: `B, C, D`
  - Data: `A, B, C, D`

### Commit E (on staging)
- **main**: 
  - History: `A`
  - Data: `A`
- **staging**: 
  - History: `B, C, D, E`
  - Data: `A, B, C, D, E`

### Commit F (on staging, removed D and E folders)
- **main**: 
  - History: `A`
  - Data: `A`
- **staging**: 
  - History: `B, C, D, E, F`
  - Data: `A, B, C, F`

### Commit G (on staging)
- **main**: 
  - History: `A`
  - Data: `A`
- **staging**: 
  - History: `B, C, D, E, F, G`
  - Data: `A, B, C, F, G (includes squash_merge.sh)`

### After Squash Merge onto Main (up to Commit G)
- **main**: 
  - History: `A, G` (G is the squashed commit from staging)
  - Data: `A, B, C, F, G`
- **staging**: 
  - History: `B, C, D, E, F, G`
  - Data: `A, B, C, F, G`

### Commit H (on staging)
- **main**: 
  - History: `A, G`
  - Data: `A, B, C, F, G`
- **staging**: 
  - History: `B, C, D, E, F, G, H`
  - Data: `A, B, C, F, G, H`

### Commit H (on staging)
- **main**: 
  - History: `A, G`
  - Data: `A, B, C, F, G`
- **staging**: 
  - History: `B, C, D, E, F, G, H`
  - Data: `A, B, C, F, G, H`

### Commit I (on staging)
- **main**: 
  - History: `A, G`
  - Data: `A, B, C, F, G`
- **staging**: 
  - History: `B, C, D, E, F, G, H, I`
  - Data: `A, B, C, F, G, H, I`

### Commit J (on staging)
- **main**: 
  - History: `A, G`
  - Data: `A, B, C, F, G`
- **staging**: 
  - History: `B, C, D, E, F, G, H, I, J`
  - Data: `A, B, C, F, G, H, I, J`

### Commit K (on staging)
- **main**: 
  - History: `A, G`
  - Data: `A, B, C, F, G`
- **staging**: 
  - History: `B, C, D, E, F, G, H, I, J, K`
  - Data: `A, B, C, F, G, H, I, J, K`

### Commit L (on staging)
- **main**: 
  - History: `A, G`
  - Data: `A, B, C, F, G`
- **staging**: 
  - History: `B, C, D, E, F, G, H, I, J, K, L`
  - Data: `A, B, C, F, G, H, I, J, K, L`

### Commit M (on staging, removed H and K folders)
- **main**: 
  - History: `A, G`
  - Data: `A, B, C, F, G`
- **staging**: 
  - History: `B, C, D, E, F, G, H, I, J, K, L, M`
  - Data: `A, B, C, F, G, I, J, L, M`

### Commit N (on staging, updated `squash_merge.sh`)
- **main**: 
  - History: `A, G`
  - Data: `A, B, C, F, G`
- **staging**: 
  - History: `B, C, D, E, F, G, H, I, J, K, L, M, N`
  - Data: `A, B, C, F, G, I, J, L, M, N`

### After Squash Merge onto Main (up to Commit N)
- **main**: 
  - History: `A, G, N` (N is the squashed commit from staging)
  - Data: `A, B, C, F, G, I, J, L, M, N`
- **staging**: 
  - History: `B, C, D, E, F, G, H, I, J, K, L, M, N`
  - Data: `A, B, C, F, G, I, J, L, M, N`

### Commit O (on staging)
- **main**: 
  - History: `A, G, N`
  - Data: `A, B, C, F, G, I, J, L, M, N`
- **staging**: 
  - History: `B, C, D, E, F, G, H, I, J, K, L, M, N, O`
  - Data: `A, B, C, F, G, I, J, L, M, N, O`

### After Squash Merge onto Main (up to Commit O)
- **main**: 
  - History: `A, G, N, O` (O is the squashed commit from staging)
  - Data: `A, B, C, F, G, I, J, L, M, N, O`
- **staging**: 
  - History: `B, C, D, E, F, G, H, I, J, K, L, M, N, O`
  - Data: `A, B, C, F, G, I, J, L, M, N, O`