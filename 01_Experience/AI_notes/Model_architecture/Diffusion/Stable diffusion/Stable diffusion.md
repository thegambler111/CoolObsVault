# 
- Stable Diffusion is a *latent* diffusion model, meaning images are represented by low-dimensional embedding, and the diffusion model works with these and produces a latent embedding that maps to our generated image (using an autoencoder)


- Now a key aspect relating to samplers is that this iterative application of our denoising neural network is equivalent to a discretized differential equation. So all these samplers that you see here are mostly just fancy ways of solving these differential equations!

![[01_Experience/AI_notes/Model_architecture/Diffusion/Stable diffusion/Diffusion sampler equations.png]]

- Basically, the DDIM & PLMS samplers were originally part of the Latent Diffusion repository.

- Here is a technical summary I wrote up of the different samplers.
![[01_Experience/AI_notes/Model_architecture/Diffusion/Stable diffusion/Diffusion samplers summary.png]]


# 

---
- Status: #done

- Tags: #diffusion

- References:
	- [Source](https://twitter.com/iScienceLuvr/status/1564847717066559488)

- Related:
	- 
