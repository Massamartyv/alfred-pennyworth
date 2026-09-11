---
file_type: strategy
venture: Paradigm
status: active
last_updated: 2026-07-26
related_files:
  - "Context/Spheres/System/Entrepreneurship/Paradigm/_index.md"
  - "Context/Spheres/System/Entrepreneurship/Paradigm/Paradigm Farms/_index.md"
---

# Paradigm Farms Build Plan v1

Owner: Martavious Spicer
Live state: Notion – The Orangery mission record, personal workspace Projects.

## Executive Summary

Paradigm Farms is the nutrition pillar of Paradigm, structured as a sub-brand with its own visual identity and voice register. The first product is a native iOS application for plant management and horticultural education, built on ARKit, RealityKit, Core ML and the Vision framework, with visionOS as the premium tier from the same codebase and Meta Ray-Ban Display and eventual Artemis glasses as the aspirational north star.

The v1 surface is a personal-use tool for the operator, backed by a Notion-only data layer, that ships with a venture-grade schema so the same model inherits when Paradigm Farms commercialises. The eventual commercial arc adds mentor-subscription pairing with working farmers, marketplace curation and community features. All deferred beyond v1.

Plant identification is layered. On-device Vision framework and a fine-tuned MobileNetV3 handle fast pre-classification. Plant.id API v3 handles species-level identification. Claude Vision handles reasoning-heavy care and diagnosis prompts. Persistent per-plant anchoring uses ARWorldMap for spatial recall with DINOv2 or Vision features layered on top for object disambiguation. Placement intelligence draws on ARKit light estimation and LiDAR scene reconstruction, with RoomPlan as the parametric room model on Pro devices.

Direction gate clears when the Validation Contract is approved. Section 8 records the five direction decisions confirmed on 2026-07-26.

## 1. Confirmed Decisions

The following were decided in the Reconnaissance conversation and are treated as inputs to this document.

- Brand architecture. Paradigm Farms is a sub-brand of Paradigm, following the Studio-under-Lululemon model. Not a pillar, not a separate marque.
- Primary platform for v1. iOS with ARKit. Vision Pro is the premium tier from the same codebase. Meta Ray-Ban Display and eventual Artemis remain the north star but do not shape v1 scope.
- Backend for v1. Notion-only. Three databases – Greenhouse for plant instances, Plant Dictionary for taxonomy, Care Events for journal entries. Migration to Supabase triggered when the app commercialises.
- Wedges for v1. Persistent journal with behavioural correction, education depth, placement intelligence. Marketplace aesthetic and community layer deferred.
- Two audiences, one tool. Home gardener leads v1 messaging. Young farmer follows once the AI layer proves itself.
- Positioning. Food-as-medicine mission carried through credible-not-fringe framing. Pro-real-food language over anti-big-pharma language.

## 2. Platform Landscape

### 2.1 Apple

Mature and directly relevant. Every v1 capability has a native path.

- ARKit 6+ provides persistent world anchoring via ARWorldMap, image tracking, object tracking via ARObjectAnchor, scene reconstruction with LiDAR and ambient light estimation. On visionOS a subset is exposed through ARKitSession with WorldTrackingProvider.
- RealityKit 3 is the stated write-once path from Apple across iOS, visionOS, iPadOS, macOS and tvOS from WWDC 2025 onward. SceneKit is deprecated. Components added at WWDC 2025 include ManipulationComponent, EnvironmentBlendingComponent, MeshInstancesComponent and ViewAttachmentComponent.
- Vision framework and Core ML support on-device image classification via VNCoreMLRequest, with models running on the Neural Engine at up to 38 TOPS on A18 or M4 silicon. Fine-tuned MobileNetV3 checkpoints run under 16 ms per inference on modern devices.
- RoomPlan produces a parametric indoor room model on LiDAR-equipped devices. This is the only first-party indoor room-type classification API across the three platforms studied.
- Developer programme. Standard Apple Developer Program at 99 USD per year. No special AR entitlement. Enterprise camera access on visionOS via CameraFrameProvider requires an additional entitlement with slower review.

### 2.2 Meta

Split into three developer contexts, each with different access levels.

- Quest platform. Meta Spatial SDK, XR Core SDK and Mixed Reality Utility Kit are open, mature and well-documented. Persistent spatial anchors, scene mesh, depth API and passthrough camera all shipping in production. The native SDK is Kotlin and Android – no port path to iOS or visionOS.
- Ray-Ban Display. Wearables Device Access Toolkit is in Developer Preview since May 2026. Build and test are open; publishing is partner-gated with broader publish access planned later in 2026. The Ray-Ban Display cannot run third-party vision models on-device – compute lives on the paired phone. Meta AI visual search is walled off from third-party apps.
- Orion and Artemis. Orion remains developer-only through 2026 and does not reach consumers. Artemis, the actual consumer-target AR glasses, is projected for 2027 or later with no public SDK yet.

The most portable gift from Meta is open-source vision infrastructure – SAM 3, SAM 3.1 Multi-Object, DINOv2 and PyTorch3D. These run wherever PyTorch, ONNX or Core ML can host them, including inside an iOS app.

### 2.3 Google

Not a v1 target. Notes for future portability and comparative benchmarking.

- ARCore is mature but Scene Semantics is outdoor-only – 12 classes covering sky, building, tree, road and similar outdoor concepts. There is no Google equivalent to Apple RoomPlan for indoor room-type classification.
- Android XR SDK is at Developer Preview 4 as of June 2026, not yet 1.0. Samsung Galaxy XR shipped in October 2025 as the competitor to Vision Pro. Android XR is not v1 territory and should not receive investment until the SDK reaches 1.0 and the installed base grows.
- Google Lens has no official API. Third-party wrappers scrape the consumer product and violate terms of service. Do not build on these.
- Gemini Vision is available via REST API but benchmarks at 28 to 48 percent accuracy on plant identification, well below Plant.id at ~85 percent top-1 and ChatGPT / GPT-4V at 54 percent.

## 3. Recommended Stack

### 3.1 iOS v1

- SwiftUI as the view layer. RealityKit as the 3D and AR runtime. ARKit as the tracking layer.
- Vision framework and Core ML for on-device inference.
- Native URLSession with lightweight Codable models for the Notion API client.
- Plant.id API v3 for species-level identification.
- Claude Vision API for care advice, disease diagnosis and behavioural correction reasoning.
- iOS 18 minimum baseline. Broader reach preserves the aspirational audience once the app opens beyond the beta.

### 3.2 Vision Pro

- Same SwiftUI + RealityKit code path with visionOS-specific session setup.
- ARKitSession + WorldTrackingProvider instead of ARWorldTrackingConfiguration.
- WorldAnchor instead of ARWorldMap for persistence.
- EnvironmentBlendingComponent for real-world occlusion of virtual plant markers in an Immersive Space.

### 3.3 Meta Ray-Ban Display

- Deferred to later 2026 when broader publish access opens.
- Thin display client of the same iOS app via the Wearables Device Access Toolkit.
- Vision computation stays on the paired iPhone. The glasses render HUD panels only.

### 3.4 Plant Identification Pipeline

1. User frames a plant. ARKit provides a stable frame.
2. On-device MobileNetV3 fine-tuned on PlantNet or PlantCLEF does a fast category pre-classification.
3. Plant.id API v3 called for species-level identification with candidate list.
4. User confirms or overrides. New Greenhouse row written to Notion.
5. Claude Vision called on demand for troubleshooting, disease diagnosis or care advice, using the confirmed species as context.

## 4. Persistent Anchoring

The requirement is that a plant labelled once is recognised on subsequent sessions without re-identification prompts. Recommended layered approach on iOS.

1. Spatial layer. ARWorldMap persisted per garden zone to FileManager with iCloud Drive sync. On session resume, load as initialWorldMap and relocalise. Each plant location is a custom AnchorEntity in the world map.
2. Visual layer. For each plant, cache a set of key-frame images and DINOv2 or Vision-framework features at label time. On session start, run visual place recognition against cached features to disambiguate multiple plants within the same anchor area.
3. Behavioural layer. Care log observations that contradict the labelled species care profile trigger the correction flow – "this plant is behaving more like X, do you want to relabel it?".

Known limitations.

- ARWorldMap relocalisation degrades in outdoor gardens with lighting and seasonal foliage changes. Store multiple maps per zone. Cue the user through relocalisation when confidence drops.
- ARObjectAnchor is tuned for tabletop-sized, textured, rigid objects. A young seedling will not track. A mature bush may. Do not rely on it as the primary identity mechanism – layer it under ARWorldMap.
- WWDC 2025 flagged a world-tracking drift regression on iOS 26.4+ LiDAR devices. Pin to a specific iOS baseline and monitor before shipping.

## 5. Placement Intelligence

Three data sources drive the wedge.

- ARFrame lightEstimate provides ambient intensity in lux and ambient colour temperature per frame. A walk-through mode samples these across rooms to build a light-condition map.
- LiDAR scene reconstruction classifies mesh regions as floor, wall, window, seat, table and similar. Window proximity is a strong proxy for light exposure. On non-LiDAR devices, plane detection alone provides a coarser fallback.
- RoomPlan builds a parametric room model on LiDAR devices and infers a room type. Cross-reference the room type with Plant Dictionary care profiles to suggest placement.

Humidity is out of scope for on-device sensing. Temperature can be inferred coarsely from HomeKit integration – deferred to v2 – or from the user logging it manually.

## 6. Portability Strategy

- iOS and visionOS. One codebase, two session-setup branches. SwiftUI and RealityKit share. Same Core ML model. Different anchor persistence – ARWorldMap on iOS, WorldAnchor on visionOS.
- Meta Ray-Ban Display. Added as a thin display client of the same iOS app once broader publish opens. Vision computation stays on the paired iPhone.
- Meta Quest. Not a v1 target. If the app ever ships to Quest, the correct path is a separate Unity-based build that shares the identification model and data schema but has its own scene, interaction and UX code.
- Android XR. Deferred to a v3+ decision once the SDK reaches 1.0 and the installed base grows meaningfully.
- Open-source vision models are the load-bearing reuse layer across all platforms. SAM 3, DINOv2, MobileNetV3 and any Plant.id-comparable model convert to Core ML, ONNX or TFLite once and ship everywhere.

## 7. Risk Register

| Risk | Severity | Mitigation |
|---|---|---|
| ARWorldMap relocalisation fails in outdoor gardens | High | Layer visual features on top of spatial anchors. Store multiple maps per zone. Cue relocalisation |
| iOS 26.4+ world tracking drift regression | Medium | Pin to a known-stable iOS baseline. Monitor Apple release notes |
| App Store health-adjacent scrutiny under Guideline 1.4 | Medium | Care advice framed as "signs consistent with", never diagnostic. Visible disclaimer. Privacy policy for camera capture |
| Plant.id pricing at scale | Medium | Batch through on-device MobileNetV3 pre-filter. Cache identifications. Negotiate tier when member count crosses 5,000 |
| Meta Ray-Ban Display publish gate does not open in 2026 | Low | Ray-Ban Display is aspirational, not v1 critical. Ship iOS and Vision Pro without dependency |
| Notion API rate limits at three requests per second | Low for v1 | Cache aggressively. Batch writes. Migrate to Supabase when member journals launch |
| Behavioural correction loop generates false positives | Medium | Confidence thresholds. Require multiple contradicting events before surfacing. User can dismiss |
| Meta closes third-party access to Ray-Ban camera | Low | Ray-Ban path is optional. iOS and Vision Pro do not depend on it |

## 8. Direction Decisions

The following were confirmed on 2026-07-26. Direction gate progression now depends on the Validation Contract being drafted and approved on top of these.

1. Repo structure. Single iOS repo named paradigm-farms-ios with a multi-target Xcode project covering iOS, visionOS and a future Meta wrapper. Restructure only when a second engineer joins.
2. Backend migration trigger. Notion-to-Supabase migration triggered by whichever lands first – first commercial member signs, app crosses 500 plant entries per user or mentor subscription launches.
3. Distribution model. TestFlight only through v1. No App Store submission until v2 when the mentor programme opens. Zero App Store review exposure in the personal-beta window.
4. iOS baseline. iOS 18 minimum. Preserves broader reach once the app opens beyond beta. No iOS 19 features required for v1.
5. Plant.id tier. Developer tier for personal beta. Commercial tier negotiation opens when Paradigm Farms takes on paying members. Zero cost commitment now.

## 9. Next Actions

Immediate work carried by the task queue.
- Build the three Notion databases – Greenhouse, Plant Dictionary, Care Events.
- Generate the Notion integration token.
- Update the Paradigm venture file with the Paradigm Farms sub-brand section.
- Draft the v1 Validation Contract.

Once the Validation Contract is approved, iOS build tasks queue.
- Xcode SwiftUI project scaffold with ARKit, RealityKit, Vision and Core ML imports.
- Notion API client and database ID configuration.
- Library and Plant Detail views, read-only from Notion.
- ARKit persistent anchor prototype. The novel piece.
- Plant.id unknown-plant identification flow.
- Care log capture with two-tap write path.
- Education card rendering from Plant Dictionary.
- Placement intelligence prototype using light estimation and LiDAR.

Direction gate clears when the Validation Contract is approved.

## Appendix – Sources

### Apple

- ARWorldMap. https://developer.apple.com/documentation/arkit/arworldmap
- Saving and loading world data. https://developer.apple.com/documentation/arkit/world_tracking/saving_and_loading_world_data
- WorldAnchor for visionOS. https://developer.apple.com/documentation/ARKit/WorldAnchor
- ARObjectAnchor. https://developer.apple.com/documentation/arkit/arobjectanchor
- Scanning and detecting 3D objects. https://developer.apple.com/documentation/ARKit/scanning-and-detecting-3d-objects
- What's new in RealityKit, WWDC 2025. https://developer.apple.com/videos/play/wwdc2025/287/
- Better together, SwiftUI and RealityKit, WWDC 2025. https://developer.apple.com/videos/play/wwdc2025/274/
- What's new in visionOS 26, WWDC 2025. https://developer.apple.com/videos/play/wwdc2025/317/
- Classifying images with Vision and Core ML. https://developer.apple.com/documentation/coreml/model_integration_samples/classifying_images_with_vision_and_core_ml
- Object Capture. https://developer.apple.com/documentation/realitykit/realitykit-object-capture/
- Reality Composer Pro. https://developer.apple.com/documentation/realitycomposerpro
- App Review Guidelines. https://developer.apple.com/app-store/review/guidelines/

### Meta

- Meta Spatial Anchors overview. https://developers.meta.com/horizon/documentation/unity/unity-spatial-anchors-overview/
- Meta Spatial SDK. https://developers.meta.com/horizon/develop/spatial-sdk/
- Introducing Meta Wearables Device Access Toolkit. https://developers.meta.com/blog/introducing-meta-wearables-device-access-toolkit/
- Meta Wearables FAQ. https://developers.meta.com/wearables/faq/
- Mesh API and Depth API for Quest 3. https://developers.meta.com/horizon/blog/mesh-depth-api-meta-quest-3-developers-mixed-reality/
- Meta Connect 2025 developer recap. https://developers.meta.com/horizon/blog/meta-connect-2025-fueling-the-future-of-vr/
- SAM 3. https://github.com/facebookresearch/sam3
- Orion to developers 2026 (UploadVR). https://www.uploadvr.com/meta-to-reportedly-offer-orion-ar-glasses-to-developers-2026/
- Artemis 2027 target (Tom's Guide). https://www.tomsguide.com/computing/vr-ar/no-not-orion-metas-first-real-ar-glasses-tipped-to-debut-in-2027

### Google

- ARCore What's New. https://developers.google.com/ar/whatsnew-arcore
- ARCore Scene Semantics. https://developers.google.com/ar/develop/scene-semantics
- ML Kit Custom Models. https://developers.google.com/ml-kit/custom-models
- Android XR I/O 2026. https://blog.google/products-and-platforms/platforms/android/android-xr-io-2026/
- Android XR SDK Developer Preview. https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html
- Gemini API Pricing. https://ai.google.dev/gemini-api/docs/pricing
- Plant.id API v3, Kindwise. https://www.kindwise.com/plant-id
- PictureThis 2025 accuracy analysis. https://gardening.alibaba.com/tips/picturethis-wins-for-plant-id-accuracy-but-only-if-you-know-this

### Cross-platform

- Unity AR Foundation. https://developers.google.com/ar/develop/unity-arf/getting-started-ar-foundation
- Cross-XR engines 2026 comparison. https://www.youngju.dev/blog/culture/2026-05-16-xr-vr-ar-dev-engines-2026-unity-xr-toolkit-unreal-5-5-vr-a-frame-three-js-webxr-meta-xr-sdk-visionos-arkit-arcore-deep-dive.en
