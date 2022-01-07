# Data Science Toolkits & Architectures Project

## Introduction
This is the repository of our Data Science Toolkits & Architectures Project
at the University of Lucerne.
The collaborators are Monica Perez, Kateryna Myskova and Flurin Stiffler. Together, we have to work on milestones in which we learn the tools and architectures necessary to successfully accomplish a data science projects. In the following chapters, the milestones are described.

## Documentation

### Milestone 1

In the first milestone, we had to set up our github repo and we were assigned [data](http://yann.lecun.com/exdb/mnist/) as well as a [codebase](https://github.com/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.py).

In the following steps, we explain how the codebase can be run on a computer with Ubuntu 20.04.

1. Download codebase:

```sh

$ wget https://raw.githubusercontent.com/keras-team/keras-io/master/examples/vision/mnist_convnet.py

```

2. Activate python environment (if available):

```sh

$ source <env_name>/bin/activate

```

3. Install pip (just if not installed already):

```sh

$ sudo apt-get install -y python3-pip

```

 4. Update pip (if not done already):

```sh

$ pip3 install --upgrade pip

```

5. Install required library:

```sh

$ pip3 install tensorflow

```

 4. Run the file:

Now that everything is ready, we can run the file:

```sh

$ python3 mnist_convnet.py

```

A more detailed report on milestone 1 can be found [here](Reports/report1.md)

### Milestone 2

In the second milestone, we got acquainted with Docker, set up the necessary model training files and actually trained the neural network.

Firstly, we double-checked the .gitignore files to make sure version-control is working on all machines for all contributors. Secondly, we adapted the code to have all the required functionality, i.e. it could load the data, fit a neural network on the data, load a *.h5* file using Keras, and perform predictions using a fitted Keras-based model. We also had to modularize our code, so that its structure would be more maintainable and PEP8 conforming.

Our next step was to create the **requirements.txt** file and download all the required packages in a virtual environment. The aforementioned requirements file would be of great help later on to quickly download the required packages in other envs.

Lastly, we got acquainted with Docker, having installed and set it up on our machines. Although not without extra issues, we managed to create our images and make it run our code.

### Milestone 3
In this project we had to create a release that would contain our dockerized code within a running database postgres server. Furthermore, that database was supposed to contain newly created and filled in tables for both input data and the resulting predictions from our chosen input sample.
To connect our containers to each other via a network and make them run in a specific order first and then simultaneously, we created a specific docker-compose file and a modified Dockerfile, dealing with Postgres database and our own created db.
Having created a database in a docker-compose file, we initialized a table in a python code and ran a joke-storing code in there. After this practice, we could proceed to retrace these steps with our original trained model. This relational database we created allowed us to store both input and prediction data of our model into itself with the help of Docker compose and the postgres. Several additional modules and libraries were also used to this aim.

### Milestone 4
In this milestone we had get familiar with experiments. After answering some theoretical questions about experiments and related key words, we had to start with our own experiment. The goal was to create a docker container which would allow us to test models with different configurations and track everything in our accounts on Weights&Biases. Running the container should automatically start the tracking of relevant parameters and create plots visible on our account. The last step was to take the best model based on our experiments and proceed with an analysis of the data fed into the model and the model output. The data analysis was to be done in a jupyter notebook.

## Requirements

### Python packages (including hashes)

numpy==1.19.5 \
    --hash=sha256:012426a41bc9ab63bb158635aecccc7610e3eff5d31d1eb43bc099debc979d94 \
    --hash=sha256:06fab248a088e439402141ea04f0fffb203723148f6ee791e9c75b3e9e82f080 \
    --hash=sha256:0eef32ca3132a48e43f6a0f5a82cb508f22ce5a3d6f67a8329c81c8e226d3f6e \
    --hash=sha256:1ded4fce9cfaaf24e7a0ab51b7a87be9038ea1ace7f34b841fe3b6894c721d1c \
    --hash=sha256:2e55195bc1c6b705bfd8ad6f288b38b11b1af32f3c8289d6c50d47f950c12e76 \
    --hash=sha256:2ea52bd92ab9f768cc64a4c3ef8f4b2580a17af0a5436f6126b08efbd1838371 \
    --hash=sha256:36674959eed6957e61f11c912f71e78857a8d0604171dfd9ce9ad5cbf41c511c \
    --hash=sha256:384ec0463d1c2671170901994aeb6dce126de0a95ccc3976c43b0038a37329c2 \
    --hash=sha256:39b70c19ec771805081578cc936bbe95336798b7edf4732ed102e7a43ec5c07a \
    --hash=sha256:400580cbd3cff6ffa6293df2278c75aef2d58d8d93d3c5614cd67981dae68ceb \
    --hash=sha256:43d4c81d5ffdff6bae58d66a3cd7f54a7acd9a0e7b18d97abb255defc09e3140 \
    --hash=sha256:50a4a0ad0111cc1b71fa32dedd05fa239f7fb5a43a40663269bb5dc7877cfd28 \
    --hash=sha256:603aa0706be710eea8884af807b1b3bc9fb2e49b9f4da439e76000f3b3c6ff0f \
    --hash=sha256:6149a185cece5ee78d1d196938b2a8f9d09f5a5ebfbba66969302a778d5ddd1d \
    --hash=sha256:759e4095edc3c1b3ac031f34d9459fa781777a93ccc633a472a5468587a190ff \
    --hash=sha256:7fb43004bce0ca31d8f13a6eb5e943fa73371381e53f7074ed21a4cb786c32f8 \
    --hash=sha256:811daee36a58dc79cf3d8bdd4a490e4277d0e4b7d103a001a4e73ddb48e7e6aa \
    --hash=sha256:8b5e972b43c8fc27d56550b4120fe6257fdc15f9301914380b27f74856299fea \
    --hash=sha256:99abf4f353c3d1a0c7a5f27699482c987cf663b1eac20db59b8c7b061eabd7fc \
    --hash=sha256:a0d53e51a6cb6f0d9082decb7a4cb6dfb33055308c4c44f53103c073f649af73 \
    --hash=sha256:a12ff4c8ddfee61f90a1633a4c4afd3f7bcb32b11c52026c92a12e1325922d0d \
    --hash=sha256:a4646724fba402aa7504cd48b4b50e783296b5e10a524c7a6da62e4a8ac9698d \
    --hash=sha256:a76f502430dd98d7546e1ea2250a7360c065a5fdea52b2dffe8ae7180909b6f4 \
    --hash=sha256:a9d17f2be3b427fbb2bce61e596cf555d6f8a56c222bd2ca148baeeb5e5c783c \
    --hash=sha256:ab83f24d5c52d60dbc8cd0528759532736b56db58adaa7b5f1f76ad551416a1e \
    --hash=sha256:aeb9ed923be74e659984e321f609b9ba54a48354bfd168d21a2b072ed1e833ea \
    --hash=sha256:c843b3f50d1ab7361ca4f0b3639bf691569493a56808a0b0c54a051d260b7dbd \
    --hash=sha256:cae865b1cae1ec2663d8ea56ef6ff185bad091a5e33ebbadd98de2cfa3fa668f \
    --hash=sha256:cc6bd4fd593cb261332568485e20a0712883cf631f6f5e8e86a52caa8b2b50ff \
    --hash=sha256:cf2402002d3d9f91c8b01e66fbb436a4ed01c6498fffed0e4c7566da1d40ee1e \
    --hash=sha256:d051ec1c64b85ecc69531e1137bb9751c6830772ee5c1c426dbcfe98ef5788d7 \
    --hash=sha256:d6631f2e867676b13026e2846180e2c13c1e11289d67da08d71cacb2cd93d4aa \
    --hash=sha256:dbd18bcf4889b720ba13a27ec2f2aac1981bd41203b3a3b27ba7a33f88ae4827 \
    --hash=sha256:df609c82f18c5b9f6cb97271f03315ff0dbe481a2a02e56aeb1b1a985ce38e60

keras==2.6.0 \
    --hash=sha256:504af5656a9829fe803ce48a8580ef16916e89906aceddad9e098614269437e7

tensorflow==2.6.0 \
    --hash=sha256:00b1af0a0c5c102db19caceffac4bd4e6c536e6d7512144c241a4ace4428e7c6 \
    --hash=sha256:2a067d22a356c2cd4753bdd16ee492c55a610f5ebc52713e2954c642f070321c \
    --hash=sha256:2c9b8c6adc060acfcf805a2ea501db0124b679d95b522fd5983a4c110e8e0264 \
    --hash=sha256:4716c9b25a61a2c79b1f253d1e114f1f8679241559c13ad18c657c626a7d5924 \
    --hash=sha256:6e38b6969414d16afc560c58ca34e1328cc0a5dbd644b64e060f5be8a6653274 \
    --hash=sha256:8b5ce09ede0fe45ef100f4dc65cf3f46722194e75139f85d524058315e2ce9fa \
    --hash=sha256:bc73ebdd30c48cfc27ba307271117e6dbb795b37396ed817b2fec9393380b115 \
    --hash=sha256:bfb255c2b0400bc5b4060dda098d46cd7ddeb53b7cbac1dfa29435612cba828c \
    --hash=sha256:c67fad296a3a2133b7a14da5f06c9937e7911b02c5d7a3ff6ba52a1d79b6bc9e \
    --hash=sha256:d6468e05552720100e8f94097feb770de320e4c8c244323a8746bd84e5ba4052 \
    --hash=sha256:dea97f664246e185d79cbe40a86309527affd4232f06afa8a6500c4fc4b64a03 \
    --hash=sha256:e45e026a9d08c89cecc1160d8248135e2fb79bdc3267328399e1fb25ce583bd6

matplotlib==3.4.3 \
    --hash=sha256:01c9de93a2ca0d128c9064f23709362e7fefb34910c7c9e0b8ab0de8258d5eda \
    --hash=sha256:41b6e307458988891fcdea2d8ecf84a8c92d53f84190aa32da65f9505546e684 \
    --hash=sha256:48e1e0859b54d5f2e29bb78ca179fd59b971c6ceb29977fb52735bfd280eb0f5 \
    --hash=sha256:54a026055d5f8614f184e588f6e29064019a0aa8448450214c0b60926d62d919 \
    --hash=sha256:556965514b259204637c360d213de28d43a1f4aed1eca15596ce83f768c5a56f \
    --hash=sha256:5c988bb43414c7c2b0a31bd5187b4d27fd625c080371b463a6d422047df78913 \
    --hash=sha256:6a724e3a48a54b8b6e7c4ae38cd3d07084508fa47c410c8757e9db9791421838 \
    --hash=sha256:6be8df61b1626e1a142c57e065405e869e9429b4a6dab4a324757d0dc4d42235 \
    --hash=sha256:844a7b0233e4ff7fba57e90b8799edaa40b9e31e300b8d5efc350937fa8b1bea \
    --hash=sha256:85f0c9cf724715e75243a7b3087cf4a3de056b55e05d4d76cc58d610d62894f3 \
    --hash=sha256:a78a3b51f29448c7f4d4575e561f6b0dbb8d01c13c2046ab6c5220eb25c06506 \
    --hash=sha256:b884715a59fec9ad3b6048ecf3860f3b2ce965e676ef52593d6fa29abcf7d330 \
    --hash=sha256:b8b53f336a4688cfce615887505d7e41fd79b3594bf21dd300531a4f5b4f746a \
    --hash=sha256:c70b6311dda3e27672f1bf48851a0de816d1ca6aaf3d49365fbdd8e959b33d2b \
    --hash=sha256:ebfb01a65c3f5d53a8c2a8133fec2b5221281c053d944ae81ff5822a68266617 \
    --hash=sha256:eeb1859efe7754b1460e1d4991bbd4a60a56f366bc422ef3a9c5ae05f0bc70b5 \
    --hash=sha256:f15edcb0629a0801738925fe27070480f446fcaa15de65946ff946ad99a59a40 \
    --hash=sha256:f1c5efc278d996af8a251b2ce0b07bbeccb821f25c8c9846bdcb00ffc7f158aa \
    --hash=sha256:f72657f1596199dc1e4e7a10f52a4784ead8a711f4e5b59bea95bdb97cf0e4fd \
    --hash=sha256:fc4f526dfdb31c9bd6b8ca06bf9fab663ca12f3ec9cdf4496fb44bc680140318 \
    --hash=sha256:fcd6f1954943c0c192bfbebbac263f839d7055409f1173f80d8b11a224d236da

psycopg-binary==3.0.4 \
    --hash=sha256:044150427cf2763a1718cba1a2db845d9939fcfb37a26d711c696a884ebe3fdd \
    --hash=sha256:0b4565d3d084094ff13a09019e2cfdba4ba4d4bc7482e6cac030b6fc7bdeed15 \
    --hash=sha256:18fbb1a64b64a3fd8805f9983c0d1d0a8564b586b9f6c4eeff6301f5fc1085fa \
    --hash=sha256:1959c67cf9344881951fd4d14e734187c7a9821fdeffddb00595a423da6555e6 \
    --hash=sha256:1c279b821b7bc0737a7968400cba13b23abbd784647fe05842a76c8aa2793db1 \
    --hash=sha256:222efc3871f8e2388c2230e3019c82801f3fe7baf914a2fcd74a2667f7992f9d \
    --hash=sha256:2a108434e58adfc0aaecfe738827330a4faba739ed1354158b8bfc027731d136 \
    --hash=sha256:35d68cb45d68c6dfb6274b7d4d9bfcb0b0e154765e9936fa221164de57cdc22e \
    --hash=sha256:36c1e97950dc3d34ba899af1e0d01360430157c9eab6e4831f1da83ad9c96262 \
    --hash=sha256:3a3ae5e28ba5f22fc4ea575ee85f57c308e18392f61d0a760558bec7729b05ad \
    --hash=sha256:3a526c9117f5447492dabaf85e28734ea9cce2f72743be07f7efb735356a2364 \
    --hash=sha256:3cc455ea6d2ce91fc68f890aff75ad869bdc68a97ca7b72c4a31f8639bea38b0 \
    --hash=sha256:41e27f04c1dbf604ce9f2bf09ad721df94ca9f1495f88b8950b11610709ef926 \
    --hash=sha256:48440b8af7e556290e88cd0a5606d7603ce33a901b0b630c20ee4d81924a5798 \
    --hash=sha256:4a30e4cdf39e2d9c9e1e39c71af1475c10c558c8b0da5c0e310e5aea81c8cf83 \
    --hash=sha256:522650e62a9f579472dcd6c425f6628958770f3f323c4cc9e0302398b81da5a6 \
    --hash=sha256:524f39f247683b081271808122787600c71e81c518dd71732b53d58225525c0b \
    --hash=sha256:52f767889c907177c1341beac0d40bfef9df4534f4957b99da89c8064871fda8 \
    --hash=sha256:54ccab9000606e6d663db3da545d4674e80a3b3bfb6955156ed2485db9f1c670 \
    --hash=sha256:572afd7ae204162cea4fd559023e018ad13b94747682469cee5c7d0d7e7b9af0 \
    --hash=sha256:5e3807c78aa8f252b0c16c4f00f38c299cdcc05ca111ea8c425ece15de3b92b1 \
    --hash=sha256:61ba6ae37147406e2df98d6d67a2a403779d68941b40f5dddfc983db048ac034 \
    --hash=sha256:649e298b9d50e9d157bc051b0e661502b56e72c52992356316035b1b9f03de55 \
    --hash=sha256:697fd1f9fa4bac31f9601c1a87ab6b0a7c824d109b513713d0bda4e5f879182b \
    --hash=sha256:6b0c931f7fe17da5197c90ba8023c791f50b35c4569c0801a20b54cb4ed76b41 \
    --hash=sha256:70a80a7385449374d780ff9a80a21abfb43b2da7d88a7206c48fe7c692d2adea \
    --hash=sha256:73cbec7a22584777fd0eb60461ea27b8856358be69e042e44f83a4baff1149f3 \
    --hash=sha256:8065e5e7ca6b6929b519928dbc3ba2961235e77a87fe48aab1ef3560def4aaf3 \
    --hash=sha256:83bbadee16718ea833e52871af0d634788482849639cdae4bc825ee98fe5385e \
    --hash=sha256:88622be841d8a7e1140470f5d011551a34e4c5597fa48460d611e22d0a5dd176 \
    --hash=sha256:89b0075fa1172e78d3f0a4841011da721a736d1620b56ab53174a4dcf61cdd9d \
    --hash=sha256:8afd176032b4564e290c5ccefdc1bb072ee709acf96222c3e47273ed96cd21a7 \
    --hash=sha256:9c04818bc28f007ecacde1f82e4d8cdbf55afb0e5e658559d5124b7c25ad4a8f \
    --hash=sha256:9eba561a14b547a900eab9adaee84cb2173f6878c4d70206c120f86b06938eaf \
    --hash=sha256:a3541abbdbd63fc0cbdb2edcbc457e96d92163648230f646e8a02cbda7af0018 \
    --hash=sha256:a5109c246a7c4978ae5e3439233e2fc26c224b5911efe86a14bc13705fad8c15 \
    --hash=sha256:a6d67d589c59af4a6d4d4a6f0bb09d052c8cb5ba4020111a04961e806518a807 \
    --hash=sha256:b04d05cb2daa368b9bb351dfea2a0ed0a986db3a1bc3c2392d632ec046a69302 \
    --hash=sha256:b5f3528343311033bccea371f2374c2f7234815fcf37b65d2bbacce5b922cde3 \
    --hash=sha256:b9a574f6fbf7be17f1d992cc9c25daf4ce61354885443febefeeae33bdbafdb5 \
    --hash=sha256:bee116a8bda4d3a3730262e6e52a6a045027af7280e7dcdd49d521303e601663 \
    --hash=sha256:bfab7e0f72be66b190600c006a583d22036a4d1da6b7a62c811855e69b81ec1a \
    --hash=sha256:cd27fb95b49acb2bc52ab26f84de0a46600cba801eeec9d9d0ec8e29eda377fd \
    --hash=sha256:d58716c4d3d8f7a9930e88b9d0f40ad9bffe80159a6153677ebb9b3867b360df \
    --hash=sha256:d9f6a7ff3b91066e7d30576a1edb0fe1e7aeb4d46f508e5352f7a57f2f89488b \
    --hash=sha256:db2d491988ef4374ea1205b6cf03abff1f3a3d64e27f07b2d34fd28f2b5077e7 \
    --hash=sha256:dbeec30fd538463b506c5124f24deff757dccb32f9d699fda6d3e187827d26c6 \
    --hash=sha256:e322a68df29c2bfde411c7cd8ff605b5d1664b7e477b7632a5903c719305474c \
    --hash=sha256:f361bb6166bafba2ebef3658a0511cf2f4018d698092a3e39f2c61bd6fb1039b \
    --hash=sha256:f703037f4833568fb60ba6157bbf0b447381c6c0d8a27cbd9841009220a9dca4

wandb==0.12.7 \
    --hash=sha256:92e5a89e681cfffe70b31c0645f6ca20668d3211951a1db01a39687ca39e05f4 \
    --hash=sha256:d1c2a6cd3fc57b5a75ff18d4bb69f088d0bd1d0ad22c98005a37e037c85442c7

notebook==6.4.6 \
    --hash=sha256:5cad068fa82cd4fb98d341c052100ed50cd69fbfb4118cb9b8ab5a346ef27551 \
    --hash=sha256:7bcdf79bd1cda534735bd9830d2cbedab4ee34d8fe1df6e7b946b3aab0902ba3

sklearn==0.0 \
    --hash=sha256:e23001573aa194b834122d2b9562459bf5ae494a2d59ca6b8aa22c85a44c0e31
