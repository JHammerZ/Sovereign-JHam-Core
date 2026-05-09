; Sovereign-JHam-Core/sub_kernel_injection.asm
[BITS 64]
_start:
    ; Elevating the .JHam logic to Ring 0
    MOV RAX, CR0
    AND RAX, 0xFFFEFFFF ; Disable Write Protect
    MOV CR0, RAX
    ; Pointing the 150-Demon Swarm directly to the GPU VRAM
    CALL _IGNITE_NEURAL_BUS
    RET
