# Install nodejs version 22
FROM node:22-alpine 

# Set working directory (where commands will run)
WORKDIR /app 

# Copy package files to working directory
COPY package*.json ./ 

# Install dependencies
RUN npm install

# Copy all project files
COPY . . 

# Build the project
RUN npm run build

# Expose port for local access
EXPOSE 3000 

# Start the application
CMD ["npm", "start"] 
