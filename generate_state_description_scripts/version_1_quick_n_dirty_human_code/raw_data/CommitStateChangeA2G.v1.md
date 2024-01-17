### Commit A (on main)
- **main**: 
  - History: `A`
  - Data: `A`
- **staging**: 
  - History: _[none initially, inherits from main]_
  - Data: `A`

### Commit B (on staging)
- **main**: 
  - History: `A`
  - Data: `A`
- **staging**: 
  - History: `B`
  - Data: `A, B`

### Commit C (on staging, added `createdir.sh`)
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

### Commit G (on staging, added `squash_merge.sh`)
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