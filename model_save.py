import torch
import torchvision

vgg16 = torchvision.models.vgg16(pretrained=False)

# Save method 1
torch.save(vgg16, 'vgg16_method1.pth')

# Save method 2 (recommended)
torch.save(vgg16.state_dict(), 'vgg16_method2.pth')