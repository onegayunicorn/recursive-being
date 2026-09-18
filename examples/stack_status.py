"""
Print unified Sovereign Stack status from Recursive Architect + bridges.
"""

from src.core.recursive_architect import RecursiveArchitect
from src.integrations.manifold_bridge import ManifoldSnapshot


def main():
    arch = RecursiveArchitect().initialize()

    # Simulate a 5D manifold snapshot (would come from PhotonicEngine.step())
    snap = ManifoldSnapshot(
        t=1.23,
        state=[0.4, 0.35, 0.45, 0.5, 0.52],
        phase=2.1,
        bio_growth=1.12,
        e_field=260.0,
        schumann_mod=1.03,
        system_coherence=0.71,
        coherence_retention_pct=98.5,
        bio_field_strength=480.0,
        feedback_active=True,
        feedback_norm=0.08,
    )
    arch.manifold.ingest(snap)

    # Simulate local-first dev engine readiness
    arch.devengine.update_handshake(paired=True, pin_active=False, device_id="local-1")
    arch.devengine.update_claw(healthy=True, last_command="status", build_ready=True)
    arch.devengine.update_paean(sync_ok=True, deploy_ok=True, root_pinned=True)

    print("\n=== Sovereign Stack Status ===\n")
    print("Recursive:", arch.status())
    print("\nManifold → Middle Flow:", arch.manifold.to_middle_flow())
    print("Manifold → Coherence:", arch.manifold.to_coherence())
    print("Manifold → Volition:", arch.manifold.to_volition())
    print("Manifold → Pulse:", arch.manifold.to_pulse())
    print("\nDevEngine:", arch.devengine.status())
    print("\nPhotonic channels:", arch.photonic.channel_list())
    print("\nSovereign ready:", arch.devengine.is_sovereign_ready())


if __name__ == "__main__":
    main()
